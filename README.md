# Text Classification API with FastAPI

## Overview

This project demonstrates how to build a simple REST API using FastAPI and explains the theoretical foundations behind modern backend systems for Machine Learning deployment.

The API receives a piece of text and returns:
- A predicted label  
- A probability score  

Although this example uses a mock classifier, the structure is designed to be easily extended to serve a real Machine Learning model (e.g., BERT, logistic regression, neural networks).

---

# Theoretical Background

## 1. What is an API?

API stands for Application Programming Interface.

In simple terms, an API allows different software systems to communicate with each other.

In web development, a REST API allows clients (websites, mobile apps, other services) to send HTTP requests to a server and receive structured responses, usually in JSON format.

Example flow:

Client → HTTP Request → Backend Server → Processing → JSON Response

---

## 2. What is a Backend?

The backend is the server-side component of an application.

It is responsible for:

- Handling HTTP requests
- Validating input data
- Running business logic
- Interacting with databases
- Running Machine Learning models
- Returning structured responses

Without a backend, a Machine Learning model remains just a local script.
With a backend, it becomes a usable service.

---

## 3. What is FastAPI?

FastAPI is a modern Python web framework for building APIs.

It is built on top of:

- Starlette (high-performance ASGI framework)
- Pydantic (data validation using Python type hints)

FastAPI leverages Python type hints to automatically:

- Validate incoming data
- Generate API documentation
- Serialize and deserialize JSON
- Provide clear error messages

---

## 4. What is ASGI?

ASGI stands for Asynchronous Server Gateway Interface.

It allows Python servers to handle multiple requests efficiently using asynchronous programming.

This makes FastAPI highly performant and suitable for production systems.

---

## 5. Why FastAPI is Popular for Machine Learning

FastAPI is widely used for ML model serving because:

- It integrates naturally with Python ML frameworks (PyTorch, TensorFlow, scikit-learn)
- It supports async operations
- It automatically generates interactive documentation
- It enforces structured input/output validation
- It scales well in microservice architectures

In modern ML systems, the typical pipeline is:

Training Phase:
Data → Model Training → Saved Model

Deployment Phase:
Client → API → Loaded Model → Prediction → Response

This project represents the deployment phase.

---

# Architecture

Client → FastAPI Backend → Model → JSON Response

Main endpoint:

POST /predict

When a request is sent:

1. FastAPI receives the HTTP request
2. Input data is validated using Pydantic schemas
3. The model function is executed
4. A structured JSON response is returned

---

# Example Request

```json
{
  "text": "This article is clearly satire."
}
```

# Example Response

```json
{
  "label": "satirical",
  "probability": 0.93
}
```

---

# Project Structure

```
text-classification-api-fastapi/
│
├── app/
│   ├── main.py        # API entry point (routing logic)
│   ├── model.py       # Prediction logic (ML layer)
│   └── schemas.py     # Data validation schemas
│
├── requirements.txt
├── README.md
└── .gitignore
```

Separation of concerns:

- main.py → Handles HTTP requests
- schemas.py → Defines data structure
- model.py → Contains model logic

This modular design reflects real-world backend architecture.

---

# Installation

Clone the repository:

```
git clone https://github.com/your-username/text-classification-api-fastapi.git
cd text-classification-api-fastapi
```

Install dependencies:

```
pip install -r requirements.txt
```

Run the server:

```
uvicorn app.main:app --reload
```

Open in browser:

http://127.0.0.1:8000/docs

FastAPI automatically generates interactive API documentation (Swagger UI).

---

# How to Extend This Project

You can replace the mock model in `model.py` with:

- A fine-tuned BERT model
- A sentiment analysis classifier
- A spam detection system
- Any NLP or ML model built with PyTorch or TensorFlow

To deploy a real model:

1. Load the trained model at startup
2. Preprocess incoming text
3. Run inference
4. Return prediction and probability

---

# Why This Project Matters

This project demonstrates:

- REST API design
- Backend architecture principles
- Data validation using schemas
- Model serving concepts
- Separation of concerns
- Production-oriented thinking

It represents the fundamental bridge between Machine Learning research and real-world application deployment.
