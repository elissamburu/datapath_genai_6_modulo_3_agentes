from pydantic import BaseModel  

class ModelRequest(BaseModel):
    user_guid: str
    question: str
    thread_id: str



