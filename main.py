from fastapi import FastAPI
from app.schemas import TextRequest, PredictionResponse
from app.model import predict_text

app = FastAPI(
    title="Text Classification API",
    description="Simple REST API built with FastAPI for text classification.",
    version="1.0.0"
)

@app.get("/")
def root():
    return {"message": "Text Classification API is running."}

@app.post("/predict", response_model=PredictionResponse)
def predict(request: TextRequest):
    label, probability = predict_text(request.text)
    return PredictionResponse(label=label, probability=probability)
