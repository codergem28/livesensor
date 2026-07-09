# 🚛 APS Fault Detection System

An end-to-end Machine Learning project that predicts failures in the Air Pressure System (APS) of heavy-duty vehicles using sensor data.

The objective of this project is to detect APS failures before they occur so that unnecessary maintenance costs can be reduced while minimizing false negatives (missed failures), which are significantly more expensive than false positives.

---

## 📌 Project Overview

The APS (Air Pressure System) is one of the most critical systems in heavy trucks.

This project builds an end-to-end production-ready Machine Learning pipeline capable of:

- Data Ingestion
- Data Validation
- Data Transformation
- Handling Missing Values
- Handling Imbalanced Dataset
- Model Training
- Model Evaluation
- Model Versioning
- Prediction using FastAPI
- Docker Deployment

The complete pipeline is automated and follows a modular MLOps-inspired architecture.

---

## Problem Statement

APS failures are rare events.

The dataset contains:

- Hundreds of sensor measurements
- Large amount of missing values
- Highly imbalanced target classes

The major challenge is reducing **False Negatives**, since failing to detect an actual APS failure can lead to expensive vehicle breakdowns.

---

## Features

- End-to-End ML Pipeline
- Automated Training Pipeline
- Automated Prediction Pipeline
- MongoDB Integration
- FastAPI REST API
- Docker Support
- Modular Project Structure
- Logging & Exception Handling
- Model Versioning
- YAML-based Configuration

---

## Tech Stack

### Programming

- Python

### Machine Learning

- Scikit-Learn
- XGBoost
- Imbalanced-Learn

### Backend

- FastAPI
- Uvicorn

### Database

- MongoDB

### Data Processing

- Pandas
- NumPy


### Configuration

- YAML
- Python Dotenv

---

## Project Architecture

```
                Dataset
                   │
                   ▼
           Data Ingestion
                   │
                   ▼
           Data Validation
                   │
                   ▼
        Data Transformation
                   │
                   ▼
        Feature Engineering
                   │
                   ▼
          Model Training
                   │
                   ▼
         Model Evaluation
                   │
                   ▼
          Saved Best Model
                   │
                   ▼
            FastAPI Server
                   │
                   ▼
         Prediction Endpoint
```

---

## Project Structure

```
APS-Fault-Detection/
│
├── artifact/
├── config/
├── prediction_file/
├── sensor/
│   ├── components/
│   ├── configuration/
│   ├── constant/
│   ├── data_access/
│   ├── entity/
│   ├── ml/
│   ├── pipeline/
│   └── utils/
│
├── logs/
├── main.py
├── requirements.txt
├── setup.py
└── README.md
```

---

## Machine Learning Pipeline

### 1. Data Ingestion

- Reads APS sensor dataset
- Stores data in MongoDB
- Splits into train and test sets

---

### 2. Data Validation

- Schema validation
- Missing column detection
- Data drift detection

---

### 3. Data Transformation

- Missing value handling
- Feature preprocessing
- Scaling
- Handling imbalanced data using SMOTETomek

---

### 4. Model Training

Models are trained and evaluated to select the best-performing classifier.

The project uses:

- XGBoost Classifier

---

### 5. Model Evaluation

Performance is evaluated while prioritizing reduction of **False Negatives** due to the high business cost of missed APS failures.

---

### 6. Model Deployment

The trained model is exposed through a FastAPI application for real-time predictions.

---

## API Endpoints

### Home

```
GET /
```

Redirects to FastAPI Swagger documentation.

---

### Train Model

```
GET /train
```

Runs the complete training pipeline.

---

### Predict

```
GET /predict
```

Loads the latest trained model and predicts APS failures from the input CSV file.

Prediction results are saved to:

```
prediction_file/prediction_output.csv
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/codergem28/APS-Fault-Detection.git
```

Move into project

```bash
cd APS-Fault-Detection
```

Create virtual environment

```bash
python -m venv venv
```

Activate environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start FastAPI server

```bash
python main.py
```

Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## Dataset

The project uses APS Failure Sensor Dataset containing over 170 sensor features collected from heavy-duty vehicles.

Target Classes:

- APS Failure
- No APS Failure

---

## Major Challenges Solved

✔ Handling large number of missing values

✔ Highly imbalanced dataset

✔ Cost-sensitive classification

✔ Reducing False Negatives

✔ Modular production-ready pipeline

✔ Model versioning

✔ Prediction API

---

## Future Improvements

- AWS Deployment
- CI/CD Pipeline
- MLflow Integration
- Model Monitoring
- Kubernetes Deployment
- Automated Retraining

---

## Author

**Sudhanshu Tripathi**

Machine Learning Engineer | AI Enthusiast

GitHub: https://github.com/codergem28

LinkedIn: https://www.linkedin.com/in/sudhanshu-mani-tripathi-a230392a3/

---

## License

This project is intended for educational and portfolio purposes.
