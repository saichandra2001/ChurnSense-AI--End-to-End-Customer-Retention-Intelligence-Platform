from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import pickle
import numpy as np

# Load model
model = pickle.load(open("churn_model.pkl", "rb"))

app = FastAPI()


# =========================
# Input Schema
# =========================
class CustomerData(BaseModel):
    credit_score: int
    gender: int
    age: float
    tenure: int
    balance: float
    products_number: int
    credit_card: int
    active_member: int
    estimated_salary: float
    country_Germany: int
    country_Spain: int


# =========================
# Home
# =========================
@app.get("/")
def home():
    return {"message": "Customer Churn Prediction API"}


# =========================
# API Prediction (Swagger)
# =========================
@app.post("/predict")
def predict(data: CustomerData):

    features = np.array([[
        data.credit_score,
        data.gender,
        data.age,
        data.tenure,
        data.balance,
        data.products_number,
        data.credit_card,
        data.active_member,
        data.estimated_salary,
        data.country_Germany,
        data.country_Spain
    ]])

    prediction = model.predict(features)[0]

    return {"prediction": int(prediction)}


# =========================
# Browser UI
# =========================
@app.get("/ui", response_class=HTMLResponse)
def ui():
    return """
    <html>
    <head>
        <title>Customer Churn Prediction</title>
    </head>
    <body>
        <h2>Customer Churn Prediction</h2>

        <form action="/predict-form" method="post">

            Credit Score: <input name="credit_score"><br><br>
            Gender (0/1): <input name="gender"><br><br>
            Age: <input name="age"><br><br>
            Tenure: <input name="tenure"><br><br>
            Balance: <input name="balance"><br><br>
            Products Number: <input name="products_number"><br><br>
            Credit Card (0/1): <input name="credit_card"><br><br>
            Active Member (0/1): <input name="active_member"><br><br>
            Estimated Salary: <input name="estimated_salary"><br><br>
            Germany (0/1): <input name="country_Germany"><br><br>
            Spain (0/1): <input name="country_Spain"><br><br>

            <button type="submit">Predict</button>

        </form>

    </body>
    </html>
    """


# =========================
# Browser Form Prediction
# =========================
@app.post("/predict-form")
def predict_form(
    credit_score: int = Form(...),
    gender: int = Form(...),
    age: float = Form(...),
    tenure: int = Form(...),
    balance: float = Form(...),
    products_number: int = Form(...),
    credit_card: int = Form(...),
    active_member: int = Form(...),
    estimated_salary: float = Form(...),
    country_Germany: int = Form(...),
    country_Spain: int = Form(...)
):

    features = np.array([[
        credit_score,
        gender,
        age,
        tenure,
        balance,
        products_number,
        credit_card,
        active_member,
        estimated_salary,
        country_Germany,
        country_Spain
    ]])

    prediction = model.predict(features)[0]

    return {"prediction": int(prediction)}