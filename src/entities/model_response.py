from pydantic import BaseModel 

class ModelResponse(BaseModel):
    user_guid: str
    question: str
    thread_id: str
    answer: str