# AIoT-Driven Indoor Air Quality Prediction

A machine learning-based system for classifying indoor air quality using environmental sensor data and the Emirati Air Quality Index (EAQI). Developed as my MSc Software Engineering final-year dissertation at Heriot-Watt University.

## Overview

Poor indoor air quality can pose significant risks to human health. This project explores how machine learning can help classify indoor air pollution levels and communicate potential health risks through a web-based application.

The system uses pollutant concentrations and environmental measurements to predict air quality categories and provide relevant health advisories.

## Key Features

- **Data Preprocessing:** Cleaning, transformation, feature engineering, and pollutant unit conversion.
- **Machine Learning:** Training and comparison of multiple classification algorithms.
- **Class Imbalance Handling:** Application of SMOTE to improve learning from underrepresented air quality categories.
- **Model Evaluation:** Stratified cross-validation using accuracy, macro-precision, macro-recall, macro F1-score, and other evaluation metrics.
- **EAQI Classification:** Classification of indoor air quality into health-related categories based on the Emirati Air Quality Index framework.
- **Web Application:** Interactive interface for entering environmental measurements and viewing predicted air quality categories.
- **Health Advisories:** Display of relevant guidance based on the predicted air quality category.
- **Model Deployment:** Saving the trained machine learning pipeline for reuse through a prediction API.

## Dataset

The project uses the *Dataset of Indoor Air Pollutants using Low-Cost Sensors*, sourced from Mendeley Data.

- **Records:** 173,468
- **Collection period:** November 2020 – July 2022
- **Location:** Pune, India
- **Measurements:** PM2.5, CO, NO₂, NH₃, O₃, temperature, humidity, and atmospheric pressure.

The dataset was selected to investigate indoor air quality prediction in the context of the Middle East, where publicly available regional datasets are limited.

## Machine Learning Approach

Thirteen machine learning algorithms were evaluated, including:

- K-Nearest Neighbors (KNN)
- Random Forest
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost
- Logistic Regression
- Linear Support Vector Machine
- Multi-Layer Perceptron (MLP)

The training pipeline incorporates robust feature scaling, class balancing, and stratified cross-validation.

**Best-performing model:** K-Nearest Neighbors (KNN), based on the reported cross-validation results.

| Metric | KNN Result |
|---|---:|
| Mean accuracy | 99.61% |
| Macro F1-score | 98.94% |

*These figures represent the reported cross-validation results, not a guarantee of real-world performance.*

## Technology Stack

- **Programming:** Python 3.10
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn, Imbalanced-learn, XGBoost, LightGBM, CatBoost
- **Visualization:** Matplotlib, Seaborn
- **Model Persistence:** Joblib
- **Backend:** Flask
- **Frontend:** React.js
- **Development:** Jupyter Notebook, VS Code, Git, GitHub

## System Workflow

1. Collect and prepare indoor air quality measurements.
2. Clean the data and engineer relevant pollutant and environmental features.
3. Train and evaluate machine learning classification models.
4. Select the best-performing model and save the trained pipeline.
5. Submit environmental measurements through the React interface.
6. Process the request through the Flask prediction API.
7. Display the predicted EAQI category and associated health advisory.

## Project Objectives

- Investigate machine learning approaches for indoor air quality classification.
- Evaluate multiple algorithms using consistent validation metrics.
- Explore the application of the EAQI framework to indoor pollutant measurements.
- Develop a web-based interface that makes model predictions accessible to users.
- Investigate the potential of AIoT-based approaches to support environmental monitoring and public health.

## Limitations and Future Work

The model was developed using data collected in Pune, India, rather than directly from indoor environments in the Middle East. Further validation using regional datasets and calibrated sensor measurements is needed before deployment in real-world healthcare or public health settings.

Potential future improvements include real-time IoT sensor integration, continuous air quality monitoring, historical trend visualization, and further validation across different indoor environments.

## Academic Project

**Degree:** MSc Software Engineering  
**University:** Heriot-Watt University  
**Research area:** Artificial Intelligence, Machine Learning, AIoT, Environmental Monitoring, and Public Health
**Grade:** S

