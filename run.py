from Utils.load_model import Predictor
from fastapi import FastAPI
import uvicorn
from Utils import load_model
import yaml

with open('path.yaml','rt') as f :
    path = yaml.safe_load(f)


predictor = Predictor(path['weights'])
app = FastAPI()

@app.get("/ping")
async def ping():
    return "Hello world"

@app.post("/predict")
async def predict(
    headline :str
):  
    names = ['Down','Up']
    prediction = predictor.predict(headline)
    return {
        'headline' : headline,
        'Trend' : names[prediction]
    }
if __name__ == '__main__' :
    uvicorn.run(app, host = 'localhost',port = 8000)