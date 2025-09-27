import numpy as np
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers.diabetes import diabetes_router

app = FastAPI()
app.include_router(diabetes_router.router)
origins = ["*"] #Toda URL puede conectar

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # quién puede hacer peticiones
    allow_credentials=True,
    allow_methods=["*"],             # permite todos los métodos: GET, POST, PUT, DELETE
    allow_headers=["*"],             # permite todas las cabeceras
)

@app.get("/")
def read_root():
    return {"Hello": "Aleja"}

