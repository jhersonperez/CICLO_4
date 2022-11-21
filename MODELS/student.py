from pydantic import BaseModel

class Students(BaseModel):
    name:str
    lastname:str
    clave:str
