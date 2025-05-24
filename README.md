![Streamlit](https://github.com/user-attachments/assets/ec74182a-696b-4ce2-9bf9-cd53679565aa)

# Diabetes Risk Prediction Web Application
 
Overview:
Built and deployed an end-to-end ML web application to predict diabetes risk using health metrics. Integrated model development, API serving, frontend interface, and cloud-native deployment.
 
## Key Contributions:
 
### Model Development:
Trained a Random Forest classifier with 95% accuracy on patient data (age, BMI, glucose, HbA1c, etc.). Performed EDA, data cleaning, cross-validation, and hyperparameter tuning using scikit-learn.
 
### Backend (API):
Built a RESTful API using FastAPI to serve predictions and expose auxiliary endpoints (gender, smoking history).
Handled data validation, request parsing, and modular utility functions.
 
### Frontend (UI):
Created an interactive interface using Streamlit where users input patient data to receive real-time predictions.
Mapped categorical inputs like “Yes/No” to binary format and enabled user-friendly dropdowns.
 
### Containerization:
Created Dockerfiles for both FastAPI and Streamlit services for environment consistency and portability.
Pushed images to Google Container Registry (GCR).
 
### Deployment on Kubernetes (GKE):
Set up a Google Kubernetes Engine (GKE) cluster using free-tier credits.
Deployed both services using Kubernetes Deployments and Services, with Ingress configured via NGINX.
Exposed only the Streamlit frontend publicly; FastAPI remained securely accessible within the cluster.
 
### Cloud DevOps:
Used Google Cloud Shell to manage deployments, build/push containers, and apply YAML configs.
Monitored resources and services via kubectl and ensured minimal cost under GCP’s free tier.
 
**Tech Stack:** Python, Scikit-learn, FastAPI, Streamlit, Docker, Kubernetes, GCP

## Data Usage

This Project uses the [Diabetes prediction dataset](https://www.kaggle.com/datasets/iammustafatz/diabetes-prediction-dataset) available on kaggle, created and uploaded by [Mohammed Mustafa](https://www.kaggle.com/iammustafatz). The dataset includes medical and demographic attributes to predict diabetes likelihood.

**Note**: The dataset is © the original author. It is used here for non-commercial, educational purposes only. It is not redistributed in this repository.
