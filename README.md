# 🚀 ML Model Deployment with CI/CD (GitHub Actions & AWS)

## 📌 Overview
This project demonstrates **end-to-end CI/CD for an ML model**, including:
- **Model Training & Testing** (with unit tests).
- **Containerization & Deployment** (via Docker & GitHub Actions).
- **AWS Deployment** using **SageMaker & ECS (Fargate)**.

---

## ⚡ Features
✅ **CI/CD Pipeline** using **GitHub Actions**  
✅ **Automated Model Deployment** to AWS **SageMaker** & **ECS**  
✅ **Three Deployment Methods:**  
- **Real-Time Endpoint (SageMaker)**
- **Serverless Inference (SageMaker Serverless)**
- **Batch Processing (SageMaker Batch Transform)**  
✅ **FastAPI-based Model API** for real-time predictions  

---

## 📂 Project Structure
```
mlops_ci_cd/
│── .github/workflows/      # CI/CD pipeline setup
│   ├── ci_cd.yml           # GitHub Actions workflow
│── data/                   # Training & test data
│── models/                 # Trained model storage
│   ├── model.tar.gz        # Model packaged for SageMaker
│── src/                    # ML model & API code
│   ├── train.py            # Model training script
│   ├── preprocess.py       # Data preprocessing
│   ├── app.py              # FastAPI model API
│── tests/                  # Unit tests
│   ├── test_train.py       # Test model training
│   ├── test_predict.py     # Test API predictions
│── requirements.txt        # Dependencies
│── Dockerfile              # Containerization for AWS ECS
│── README.md               # Project Documentation
│── client.py               # Test API Client
```

---

## 🔧 Installation & Setup

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/onehungrybird/mlops_ci_cd.git
cd mlops_ci_cd
```

### **2️⃣ Set Up Python Environment**
```sh
python -m venv venv
source venv/bin/activate   # (Mac/Linux)
venv\Scripts\activate      # (Windows)
pip install -r requirements.txt
```

### **3️⃣ Train the Model**
```sh
python src/train.py
```
This will save a trained model inside the **`models/`** directory.

### **4️⃣ Run the API Locally**
```sh
uvicorn src.app:app --host 0.0.0.0 --port 8000
```
Test API:
```sh
curl -X POST "http://localhost:8000/predict/" \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

---

## ☁️ **AWS Deployment Methods**
### **1️⃣ Deploy as a Real-Time Endpoint (SageMaker)**
```sh
aws s3 cp models/model.tar.gz s3://your-s3-bucket/mlops_model/
python deploy_sagemaker.py
```
✅ **Best for:** **Low-latency APIs (Chatbots, Recommendations)**  

---

### **2️⃣ Deploy as Serverless Inference (SageMaker)**
```sh
python create_serverless.py
```
✅ **Best for:** **On-demand ML inference (Fraud Detection, OCR)**  
⏳ **Has cold start (1-5 sec per request).**  

---

### **3️⃣ Deploy as Batch Processing (SageMaker Batch Transform)**
```sh
python run_batch_job.py
```
✅ **Best for:** **Processing large datasets at once (Customer Churn, Risk Analysis)**  

---

## **🚀 Deploy ML Model to AWS ECS (Fargate)**
### **1️⃣ Push Docker Image to AWS ECR**
```sh
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <aws-account-id>.dkr.ecr.us-east-1.amazonaws.com
docker tag ghcr.io/onehungrybird/mlops_ci_cd:latest <aws-account-id>.dkr.ecr.us-east-1.amazonaws.com/mlops_ci_cd:latest
docker push <aws-account-id>.dkr.ecr.us-east-1.amazonaws.com/mlops_ci_cd:latest
```

### **2️⃣ Deploy to AWS ECS**
- **Create ECS Cluster & Task Definition**
- **Deploy ML Model as a service**

Test API after deployment:
```sh
curl -X POST "http://<ecs-public-ip>:8000/predict/" \
     -H "Content-Type: application/json" \
     -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```

---

## **📝 Final Takeaways**
✔ **SageMaker Built-in Images** allow deployment **without Docker**.  
✔ **Serverless ML** is **cheaper but has cold starts**.  
✔ **ECS is better if you need a FastAPI-based custom ML API**.  
✔ **Batch Transform is best for processing large datasets efficiently**.  

---

🚀 **Happy Deploying!** 🔥
