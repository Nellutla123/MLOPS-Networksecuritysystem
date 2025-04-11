
---

# 🛡️ MLOps Project - Network Security System for Phishing Data

Phishing data refers to sensitive personal information such as passwords, bank details, or credit card numbers that cybercriminals attempt to acquire through deceptive means.

This project focuses on building an **MLOps-based network security system** to detect phishing attempts by classifying data as malicious or non-malicious. The solution leverages **ETL pipelines**, **machine learning models**, and **cloud deployment** to ensure a robust, scalable, and production-ready application.

---

## 🎯 Objective

To predict whether phishing data is **malicious** or **non-malicious** using a structured MLOps workflow with an emphasis on **automation**, **scalability**, and **reproducibility**.

---

## ⚙️ Key Components and Workflow

### 🔁 Data Pipeline

- **ETL Pipeline**: Created pipelines to extract, transform, and load data into a **MongoDB** instance.
- **Data Ingestion**: Phishing data was ingested from MongoDB, split into train/test sets, and stored as ingestion artifacts.
- **Data Validation**: Ensured data consistency using **data drift parameters**.
- **Data Transformation**: Preprocessed the data and saved a `preprocessor.pkl` file.

### 🤖 Model Development

- **Model Training**: Trained multiple models:
  - Logistic Regression  
  - K-Nearest Neighbors (KNN)  
  - AdaBoost  
  - Decision Tree  
  - Random Forest
- **Model Evaluation**: Selected the best-performing model and saved it as `model.pkl`.
- **Pipelines**: Built separate pipelines for **training** and **batch prediction**.

### 📊 Experiment Tracking and Artifact Management

- Used **DagsHub** integrated with **MLflow** to:
  - Track experiments
  - Log metrics
  - Manage model selection
- Stored all major artifacts (e.g., `preprocessor.pkl`, `model.pkl`) in **AWS S3** for versioning and persistence.

### 🌐 Web Application

- Developed a real-time prediction service using **FastAPI**.

### ☁️ Cloud Deployment

- **Dockerization**: Created and pushed a Docker image to **AWS Elastic Container Registry (ECR)**.
- **CI/CD**: Automated deployment via **GitHub Actions**.
- **Deployment**: Hosted the application on an **AWS EC2** instance.

---

## 🧰 Technologies and Tools Used

| Category | Tools |
|----------|-------|
| **Data Storage** | MongoDB, AWS S3 |
| **MLOps Tools** | DagsHub, MLflow |
| **Machine Learning** | Scikit-learn (Logistic Regression, KNN, AdaBoost, Decision Tree, Random Forest) |
| **Web Framework** | FastAPI |
| **Cloud Services** | AWS EC2, ECR, S3 |
| **Automation & CI/CD** | GitHub Actions |
| **Containerization** | Docker |

---

## ✅ Outcome

This project successfully delivers an end-to-end MLOps pipeline for **phishing detection**, integrating:

- Data ingestion and preprocessing  
- Model training, evaluation, and artifact logging  
- Automated deployment to AWS  
- Real-time prediction via FastAPI  

The final system is deployed on **AWS EC2**, capable of handling phishing detection in real-world scenarios, with complete **reproducibility**, **scalability**, and **automated monitoring**.




