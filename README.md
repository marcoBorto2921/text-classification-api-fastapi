# Text Classification API with FastAPI

## Overview

This project demonstrates how to build a simple REST API using FastAPI.

The API receives a piece of text and returns:
- A predicted label  
- A probability score  

This example uses a mock classifier for demonstration purposes, but it can easily be extended to serve a real Machine Learning model (e.g., BERT, logistic regression, etc.).

---

## What is FastAPI?

FastAPI is a modern Python web framework for building APIs.

It is built on top of:
- Starlette (high-performance ASGI framework)
- Pydantic (data validation using Python type hints)

### Why use FastAPI?

- High performance (ASGI-based)
- Automatic request validation
- Automatic interactive API documentation (Swagger UI)
- Easy integration with Machine Learning models
- Clean and modern Python design
- Async support out of the box

FastAPI is widely used for deploying Machine Learning models in production environments.

---

## Architecture

Client → FastAPI Backend → Model → JSON Response

Main endpoint:

POST /predict

---

## Example Request

```json
{
  "text": "This article is clearly satire."
}
```

## Example Response

```json
{
  "label": "satirical",
  "probability": 0.93
}
```

---

## Project Structure

```
text-classification-api-fastapi/
│
├── app/
│   ├── main.py
│   ├── model.py
│   └── schemas.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

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

You will see the automatically generated interactive documentation.

---

## How to Extend This Project

You can replace the mock model in `model.py` with:

- A fine-tuned BERT model
- A sentiment analysis classifier
- A spam detection system
- Any NLP or ML model built with PyTorch or TensorFlow

Simply load your trained model inside `model.py` and return the prediction output.

---

## Why This Project Matters

This project demonstrates:

- API development with FastAPI  
- Backend fundamentals  
- Clean and scalable project structure  
- Model serving concepts  
- Production-oriented thinking  

It is a solid starting point for deploying Machine Learning systems as web services.
