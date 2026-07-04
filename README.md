#  ChurnSense-AI
### End-to-End Customer Retention Intelligence Platform using Machine Learning, FastAPI, Docker & AWS EC2

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)
![XGBoost](https://img.shields.io/badge/Model-XGBoost-orange)
![Docker](https://img.shields.io/badge/Docker-Container-blue)
![AWS](https://img.shields.io/badge/AWS-EC2-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

##  Project Overview

**ChurnSense-AI** is an end-to-end Machine Learning application that predicts whether a bank customer is likely to churn based on demographic and financial information.

Unlike traditional prediction systems that only return a classification result, this project integrates a **Large Language Model (LLM)** through the **Hugging Face Inference API** to generate natural language business explanations for every prediction.

The entire solution is built as a production-ready REST API using **FastAPI**, containerized with **Docker**, and deployed on an **AWS EC2 (Ubuntu)** server.

This project demonstrates the complete Machine Learning deployment lifecycle—from data preprocessing and model training to API development, containerization, and cloud deployment.

---

#  Features

- Customer Churn Prediction
- XGBoost Machine Learning Model
- AI-generated Business Explanations using LLM
- FastAPI REST API
- Interactive Swagger Documentation
- Docker Containerization
- AWS EC2 Deployment
- Production-ready API Architecture

---

#  Project Architecture

```
                    User
                      │
                      ▼
                FastAPI REST API
                      │
         ┌────────────┴────────────┐
         ▼                         ▼
  XGBoost Model          Hugging Face LLM
         │                         │
         ▼                         ▼
 Customer Churn          Business Explanation
         │                         │
         └────────────┬────────────┘
                      ▼
                JSON Response
```

---

#  Tech Stack

## Machine Learning

- Python
- Scikit-learn
- XGBoost
- Pandas
- NumPy

## Backend

- FastAPI
- Uvicorn
- Pydantic

## AI / LLM

- Hugging Face Inference API
- Meta Llama 3.3-70B-Instruct

## Deployment

- Docker
- AWS EC2
- Ubuntu Linux

---

#  Project Structure

```text
customer-churn/
│
├── app.py
├── llm.py
├── Dockerfile
├── requirements.txt
├── churn_model.pkl
├── scaler.pkl
├── gender_encoder.pkl
├── Bank Customer Churn Prediction.csv
├── ML Learning.ipynb
└── README.md
```

---

#  Machine Learning Workflow

## 1️ Data Collection

- Bank Customer Churn Dataset

---

## 2️ Data Preprocessing

- Missing Value Analysis
- Feature Selection
- Label Encoding
- Feature Scaling

---

## 3️ Exploratory Data Analysis (EDA)

- Customer Distribution
- Correlation Analysis
- Feature Visualization

---

## 4️ Feature Engineering

- Data Transformation
- Encoding
- Scaling

---

## 5️ Model Training

Models Used

- Random Forest (Baseline)
- XGBoost Classifier (Final Model)

---

## 6️ Model Evaluation

- Accuracy
- Confusion Matrix
- Classification Report

---

## 7️ Hyperparameter Tuning

Improved model performance using parameter optimization.

---

## 8️ Model Serialization

Saved artifacts:

```
churn_model.pkl
scaler.pkl
gender_encoder.pkl
```

---

#  FastAPI Development

The application exposes REST APIs for customer churn prediction.

## Endpoints

### GET /

Returns API health status.

---

### POST /predict

Predicts customer churn and returns an AI-generated business explanation.

---

### Swagger Documentation

```
http://localhost:8000/docs
```

---

#  Sample API Response

```json
{
  "prediction": 1,
  "prediction_text": "Customer is likely to churn",
  "AI_explanation": "This customer may churn due to a relatively low credit score, inactive membership, and limited engagement with banking services."
}
```

---

#  Dockerization

The application is containerized using Docker for consistent deployment across environments.

## Docker Workflow

```
Application
      │
Dockerfile
      │
Docker Image
      │
Docker Container
```

## Build Docker Image

```bash
docker build -t customer-churn-app .
```

## Run Container

```bash
docker run -d -p 8000:8000 --name customer-churn-container customer-churn-app
```

## Verify Running Container

```bash
docker ps
```

---

#  AWS EC2 Deployment

The application is deployed on an Ubuntu EC2 instance.

## Step 1

Launch an Ubuntu EC2 Instance.

---

## Step 2

Connect using SSH.

```bash
ssh -i customer-key.pem ubuntu@<EC2-PUBLIC-IP>
```

---

## Step 3

Update Ubuntu.

```bash
sudo apt update
sudo apt upgrade -y
```

---

## Step 4

Install Docker.

```bash
sudo apt install docker.io -y
```

Verify Installation

```bash
sudo systemctl status docker
```

---

## Step 5

Upload Project.

```bash
scp -i customer-key.pem -r . ubuntu@<EC2-PUBLIC-IP>:~/customer-churn
```

---

## Step 6

Build Docker Image.

```bash
cd ~/customer-churn

sudo docker build -t customer-churn-app .
```

---

## Step 7

Run Docker Container.

```bash
sudo docker run -d \
-p 8000:8000 \
--name customer-churn-container \
customer-churn-app
```

---

## Step 8

Verify Container.

```bash
sudo docker ps
```

---

## Step 9

Configure Security Group

Open Port

```
8000
```

Source

```
0.0.0.0/0
```

---

## Step 10

Open Swagger UI

```
http://<EC2-PUBLIC-IP>:8000/docs
```

---

#  Challenges Faced

During deployment, several real-world issues were encountered and successfully resolved.

- UTF-16 to UTF-8 requirements file conversion
- Docker build failures
- Missing Python packages
- EC2 disk storage limitations
- Root partition expansion
- Docker installation issues
- AWS Security Group configuration
- SSH authentication
- Docker networking

These challenges provided valuable hands-on experience in Linux administration and cloud deployment.

---

#  Skills Demonstrated

### Machine Learning

- Data Preprocessing
- Feature Engineering
- XGBoost Classification
- Model Serialization

### Backend

- FastAPI
- REST API Development
- Swagger Documentation

### AI Integration

- Hugging Face API
- Meta Llama 3.3
- Prompt Engineering

### Cloud Computing

- AWS EC2
- Ubuntu
- SSH
- Security Groups

### Containerization

- Docker
- Docker Images
- Docker Containers

### Linux

- Package Management
- SCP
- Server Administration

---

#  Future Improvements

- GitHub Actions CI/CD
- Nginx Reverse Proxy
- HTTPS with Let's Encrypt
- Custom Domain
- Monitoring & Logging
- Automatic Docker Restart
- Production Deployment Pipeline
- Kubernetes Deployment
- Model Versioning
- Database Integration

---

#  Author

**Sai Chandra Prasad P**

AI Engineer • Machine Learning Engineer • Data Scientist

---

# ✅ Project Status

- ✅ Machine Learning Model Completed
- ✅ FastAPI REST API Completed
- ✅ Swagger Documentation Completed
- ✅ Docker Containerization Completed
- ✅ AWS EC2 Deployment Completed
- ✅ Hugging Face LLM Integration Completed

---

## ⭐ If you found this project helpful, consider giving it a Star!
