# ChurnSense-AI-End-to-End-Customer-Retention-Intelligence-Platform with FastAPI, Docker & AWS EC2

## Project Overview

This project predicts whether a bank customer is likely to churn based on customer information using a Machine Learning model. The model is deployed as a REST API using FastAPI, containerized with Docker, and hosted on an AWS EC2 Ubuntu server.

The objective of this project is to demonstrate an end-to-end Machine Learning deployment pipeline, starting from model training to cloud deployment.

---

# Project Architecture

```
Customer Data
      │
      ▼
Machine Learning Model (XGBoost)
      │
      ▼
FastAPI REST API
      │
      ▼
Docker Container
      │
      ▼
AWS EC2 (Ubuntu)
      │
      ▼
Public API (Swagger UI)
```

---

# Technologies Used

* Python 3.11
* FastAPI
* Uvicorn
* Scikit-learn
* XGBoost
* Pandas
* NumPy
* Docker
* AWS EC2
* Ubuntu Linux
* Pickle

---

# Project Structure

```
customer-churn/
│
├── app.py
├── Dockerfile
├── requirement.txt
├── churn_model.pkl
├── scaler.pkl
├── gender_encoder.pkl
├── Bank Customer Churn Prediction.csv
├── ML Learning.ipynb
└── README.md
```

---

# Machine Learning Workflow

### Data Collection

* Bank Customer Churn dataset

### Data Preprocessing

* Missing value checking
* Feature selection
* Label Encoding
* Feature Scaling

### Model Training

Algorithm Used:

* XGBoost Classifier

### Model Serialization

Saved files:

* churn_model.pkl
* scaler.pkl
* gender_encoder.pkl

---

# FastAPI Development

Created REST API using FastAPI.

### Available Endpoints

```
GET /
```

Returns API status.

```
POST /predict
```

Accepts customer details and predicts customer churn.

Swagger Documentation:

```
/docs
```

---

# Dockerization

Created Dockerfile to containerize the application.

Docker Workflow

```
Application
     │
Dockerfile
     │
Docker Image
     │
Docker Container
```

Docker Build

```bash
docker build -t customer-churn-app .
```

Docker Run

```bash
docker run -d -p 8000:8000 --name customer-churn-container customer-churn-app
```

Verify Running Container

```bash
docker ps
```

---

# AWS EC2 Deployment

Created an Ubuntu EC2 instance on AWS.

Deployment Steps

### 1. Launch EC2 Instance

* Ubuntu Server
* Security Group configured
* SSH Key Pair created

### 2. Connect to EC2

```bash
ssh -i customer-key.pem ubuntu@<EC2-PUBLIC-IP>
```

---

### 3. Update Ubuntu

```bash
sudo apt update
sudo apt upgrade -y
```

---

### 4. Install Docker

```bash
sudo apt install docker.io -y
```

Verify Installation

```bash
sudo systemctl status docker
```

---

### 5. Upload Project

Copied the complete project from the local machine to EC2 using SCP.

```bash
scp -i customer-key.pem -r . ubuntu@<EC2-PUBLIC-IP>:~/customer-churn
```

---

### 6. Build Docker Image

```bash
cd ~/customer-churn

sudo docker build -t customer-churn-app .
```

---

### 7. Run Docker Container

```bash
sudo docker run -d \
-p 8000:8000 \
--name customer-churn-container \
customer-churn-app
```

---

### 8. Verify Container

```bash
sudo docker ps
```

---

### 9. Configure AWS Security Group

Opened Custom TCP Port:

```
8000
```

Source:

```
0.0.0.0/0
```

---

### 10. Access Swagger UI

```
http://<EC2-PUBLIC-IP>:8000/docs
```

The API is now publicly accessible through AWS EC2.

---

# Challenges Faced

During deployment, several real-world issues were encountered and resolved.

* Requirement file encoding issue (UTF-16 to UTF-8)
* Docker image build failures
* Missing Python dependencies
* EC2 storage limitations
* Root partition size issues
* Docker installation and configuration
* AWS Security Group configuration
* SSH authentication
* Docker container networking

Resolving these issues provided valuable hands-on experience with cloud deployment and Linux system administration.

---

# Skills Demonstrated

Machine Learning

* Data preprocessing
* Feature engineering
* XGBoost Classification
* Model serialization

Backend Development

* FastAPI
* REST API Development
* Swagger Documentation

Containerization

* Docker
* Docker Image Creation
* Docker Container Management

Cloud Computing

* AWS EC2
* Ubuntu Server
* SSH
* Security Groups

Linux

* Package Management
* Docker Installation
* File Transfer using SCP
* Server Administration

---

# Future Improvements

* GitHub Actions CI/CD
* Nginx Reverse Proxy
* HTTPS using Let's Encrypt
* Custom Domain
* Hugging Face LLM Integration
* AI-powered Customer Churn Explanation
* Monitoring and Logging
* Automatic Docker Restart Policy
* Production Deployment Pipeline

---

# Author

Sai Chandra Prasad P

AI Engineer | Machine Learning Engineer | Data Scientist

---

# Project Status

-> Machine Learning Model Completed

-> FastAPI REST API Completed

-> Swagger Documentation Completed

-> Docker Containerization Completed

-> AWS EC2 Deployment Completed

