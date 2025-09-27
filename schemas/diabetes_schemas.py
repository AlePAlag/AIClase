from pydantic import BaseModel

class PatientData(BaseModel):
    first_name:str
    last_name: str
    identification_number:str
    pregnancies:int
    glucose:int
    bloodpressure: int
    skinthickness:int
    insulin:int
    bmi:float
    diabetespedigreefunction:float
    age:int