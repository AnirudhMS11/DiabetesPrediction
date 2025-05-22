from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import util
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    util.load_artifacts()
    yield

app = FastAPI(lifespan=lifespan)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

 
@app.get("/get-gender")
def getGender():
    return JSONResponse(content={"gender": util.get_gender()})

@app.get("/get-smoking")
def getSmokingHistory():
    return JSONResponse(content={"smoking_history": util.get_smoking_history()})

@app.post('/get-prediction')
def getPrediction(
    age: float = Form(...),
    hypertension: int = Form(...),
    heart_disease: int = Form(...),
    bmi: float = Form(...),
    HbA1c_level: float = Form(...),
    blood_glucose_level: int = Form(...),
    gender: str = Form(...),
    smoking_history: str = Form(...)
):
    prediction = util.get_Prediction(age,hypertension,heart_disease,bmi,HbA1c_level,
                                     blood_glucose_level,gender,smoking_history)
    return JSONResponse(content={"Prediction": int(prediction)})