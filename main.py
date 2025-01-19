from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv 
from src.entities.model_request import ModelRequest
from src.entities.model_response import ModelResponse
from src.graph.graph import graph
from IPython.display import Image, display
# Cargar variables de entorno  
load_dotenv() 

# Crear la aplicación FastAPI
app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/v1/init-about-us")
async def init_about_us():
    '''  
        Endpoint para obtener la información de la empresa
    '''
    from langchain_core.documents import Document
    from langchain.document_loaders import UnstructuredMarkdownLoader,  TextLoader
    from langchain.text_splitter import CharacterTextSplitter
    markdown_path = "./src/about_us.md"

    from langchain_text_splitters import MarkdownHeaderTextSplitter
    headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
    ("###", "Header 3"),
    ]
    
    # loader = UnstructuredMarkdownLoader(markdown_path, text_splitter=markdown_splitter)
    loader = TextLoader(markdown_path)
    # md = '# Foo\n\n ## Bar\n\nHi this is Jim  \nHi this is Joe\n\n ## Baz\n\n Hi this is Molly' 
    documents = loader.load()
    print(documents[0].page_content[:1000])

    markdown_splitter = MarkdownHeaderTextSplitter(headers_to_split_on)
    md_header_splits = markdown_splitter.split_text(documents[0].page_content)
    #  md_header_splits = markdown_splitter.split_text(documents[0].page_content)
    
    print('#################')
    print(len(md_header_splits))
    for sentence in md_header_splits:
        print('>>>>>>>>>>>>>>>>>>>>>>> ')
        print(sentence.page_content[:50])
    #    print(sentence.page_content)
    print('#################')
    #from langchain_openai import ChatOpenAI

    #llm = ChatOpenAI(model_name="gpt-4o")

    #for text_chunk in split_sentences:
    #    summary = llm.predict("Summarize this text: " + text_chunk.page_content)
        #print(summary)

    from src.utils.vectorStore import upload_data
    upload_data(md_header_splits,"about_us")

    from src.tools.sobre_nosotros import sobre_nosotros_retriever_tool
    tool = sobre_nosotros_retriever_tool()
    resultas = tool.invoke("Cuál es el nombre de la empresa?")
    print ("Retrieval")
    print(resultas)
    return True


@app.post("/api/v1/chat")
async def chat_endpoint(request: ModelRequest) -> ModelResponse:
    '''  
        Endpoint para chatear con el sistema de agentes
    '''
    from langchain.globals import set_debug

    set_debug(False)

    # Create the directory if it doesn't exist
    os.makedirs("graphs", exist_ok=True)
    
    # Save the graph image to a file
    graph_image = graph.get_graph(xray=True).draw_mermaid_png()
    graph_path = "graphs/graph.png"
    with open(graph_path, "wb") as f:
        f.write(graph_image)
    
    # Display the saved image
    display(Image(graph_path), metadata={"image/png": "Graph"})

    config = {"configurable": {"thread_id": "7"}}

    response1 = graph.invoke({"messages": [("user", request.question)]}, subgraphs=True, config=config)
    """print("##############################################")
    print(response1)
    print('<<<<<<<<<<<<<<<<<')
    print(response1[0])
    print('>>>>>>>>>>>>>>>>>')
    print(response1[1])
    print('#################')
    for message in response1[1]["messages"]:
        print(message)

    print("##############################################")
    print(response1[1]["messages"][-1].content)
    print("##############################################")"""
    
    return ModelResponse(
        user_guid=request.user_guid,
        question=request.question,
        thread_id=request.thread_id,
        answer=response1[1]["messages"][-1].content.replace("FINAL RESPONSE:\n", " "),
    )


@app.get("/productos")
async def obtener_productos():
    '''  
        Endpoint para obtener la lista de productos
    '''
    from src.tools.productos import products_tool
    client = products_tool()
    return client.consultar_productos();

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)


# uvicorn main:app --host 0.0.0.0 --port 8002 --reload    

# http://localhost:8002/docs
# http://localhost:8002/redoc


"""
{
  "user_guid": "1240413m2lm",
  "question": "Puedes trarme un listado de productos?",
  "thread_id": "15416351"
}
"""