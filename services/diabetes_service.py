
import pickle

import numpy as np
from schemas.diabetes_schemas import PatientData # pyright: ignore[reportMissingImports, reportUndefinedVariable] #


with open('RFDiabetesv132.pkl','rb') as file:
    RF_model2 = pickle.load(file)

labels = ["Sano","Enfermo"]

def diabetes_prediction(data:PatientData):

    xin= np.array([
        data.pregnancies,
        data.glucose,
        data.bloodpressure,
        data.skinthickness,
        data.insulin,
        data.bmi,
        data.diabetespedigreefunction,
        data.age
    ]).reshape(1,8) # numero de filas y columnas 
    prediction = RF_model2.predict(xin)
    print("prediction", prediction)

    return labels[prediction[0]]
