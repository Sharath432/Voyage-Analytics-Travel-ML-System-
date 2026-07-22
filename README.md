# ✈️ Voyage Analytics: Travel Intelligence using Machine Learning

## Project Overview

Voyage Analytics is an end-to-end Machine Learning project developed for the travel and tourism domain. The project demonstrates how predictive analytics and recommendation systems can improve travel-related decision making.

The project consists of three independent machine learning modules:

- Flight Price Prediction (Regression)
- Gender Classification (Classification)
- Hotel Recommendation System (Recommendation Engine)

These models demonstrate the application of supervised learning, recommendation systems, feature engineering, model evaluation, and deployment concepts using Flask.

---

# Business Problem

Travel companies generate large volumes of customer, flight, and hotel booking data.

This project aims to leverage this data to:

- Predict flight prices
- Classify customer gender
- Recommend suitable hotels
- Demonstrate deployment using Flask REST API

---

# Dataset

The project uses three datasets.

### Users Dataset

Contains customer information such as:

- User ID
- Name
- Company
- Gender
- Age

### Flights Dataset

Contains:

- Travel Code
- User Code
- Boarding City
- Destination
- Flight Type
- Flight Agency
- Distance
- Flight Duration
- Flight Price
- Travel Date

### Hotels Dataset

Contains:

- Hotel Name
- Hotel Location
- Number of Days
- Price Per Day
- Total Cost
- Booking Date

---

# Project Modules

## 1. Flight Price Prediction

### Objective

Predict the flight ticket price using regression algorithms.

### Techniques Used

- Data Cleaning
- Feature Engineering
- One-Hot Encoding
- Feature Scaling
- Feature Selection
- Model Evaluation
- Hyperparameter Tuning

### Models Implemented

- Linear Regression
- Ridge Regression
- Lasso Regression
- ElasticNet
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor

### Evaluation Metrics

- RMSE
- MAE
- R² Score

---

## 2. Gender Classification

### Objective

Predict customer gender based on user information.

### Models Used

- Logistic Regression
- Decision Tree
- Random Forest
- Gradient Boosting

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

---

## 3. Hotel Recommendation System

### Objective

Recommend suitable hotels based on user preferences.

### Recommendation Techniques

- Content-Based Filtering
- Collaborative Filtering (SVD)

### Evaluation

- Recall@K
- Top-N Recommendation

---

# Flask REST API

The Flight Price Prediction model is deployed using Flask.

The application:

- Accepts flight details from users
- Performs preprocessing
- Loads the trained regression model
- Predicts flight prices
- Returns prediction results through REST API

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Flask
- Pickle
- Matplotlib
- Seaborn
- Google Colab

---

# Repository Structure

```
Flight_Price_Regression_Model.ipynb
Gender_Classification_Model.ipynb
Hotel_Recommendation_System.ipynb
datasets/
README.md
requirements.txt
```

---

# Future Improvements

Potential production enhancements include:

- Docker containerization
- Kubernetes deployment
- MLflow model tracking
- Apache Airflow workflow automation
- Jenkins CI/CD pipeline
- Streamlit dashboard
- Cloud deployment (AWS/Azure)

---

# Learning Outcomes

Through this project, I gained hands-on experience in:

- Machine Learning workflows
- Feature Engineering
- Regression and Classification
- Recommendation Systems
- Model Evaluation
- Hyperparameter Tuning
- Flask API Development
- End-to-End ML Project Development

---

# Author

**Sarathraj R**

LinkedIn: https://www.linkedin.com/in/sarathraj-r-ds/
