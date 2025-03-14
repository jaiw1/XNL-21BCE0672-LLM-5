from fastapi import FastAPI
import onnxruntime as ort
import numpy as np

app = FastAPI()

# Load the ONNX model
session = ort.InferenceSession("gpt2.onnx")

@app.get("/")
def home():
    return {"message": "LLM API is running"}

@app.post("/predict")
def predict(input_ids: list):
    input_tensor = np.array(input_ids, dtype=np.int64).reshape(1, -1)
    outputs = session.run(None, {"input": input_tensor})
    return {"output": outputs[0].tolist()}
