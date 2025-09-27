from fastapi import APIRouter

from schemas.diabetes_schemas import PatientData
from services.diabetes_service import diabetes_prediction


router = APIRouter()


@router.post("/predict") # type: ignore
async def patient_predict(data: PatientData):
    print("patient data ", data.identification_number)

    prediction = diabetes_prediction(data)

    return{"prediction": prediction}
