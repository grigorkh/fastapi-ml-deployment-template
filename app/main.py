from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

app = FastAPI()

# Load the model
with open("model/iris_model.pkl", "rb") as f:
    model = pickle.load(f)

class IrisFeatures(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(features: IrisFeatures):
    input_data = np.array([[features.sepal_length, features.sepal_width,
                            features.petal_length, features.petal_width]])
    prediction = model.predict(input_data)[0]
    return {"prediction": int(prediction)}
