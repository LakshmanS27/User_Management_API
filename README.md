# User Management System

A simple **User Management API** built using **FastAPI**, **SQLite**, **Redis**, and **Streamlit**.  
This project demonstrates CRUD operations, caching with Redis, and a basic UI using Streamlit.

---

## Tech Stack

- FastAPI – Backend REST API  
- SQLite – Database  
- SQLAlchemy – ORM  
- Redis – Caching  
- Streamlit – Frontend UI  
- Uvicorn – ASGI server  

---

## Features

- Create, Read, and Delete users
- Redis caching for faster read operations
- SQLite database for persistent storage
- Streamlit dashboard for easy interaction
- Email uniqueness validation

---

## Database Schema

```python
id = Column(Integer, primary_key=True, index=True)
name = Column(String, nullable=False)
age = Column(Integer, nullable=False)
email = Column(String, unique=True, index=True, nullable=False)
city = Column(String, nullable=False)
phone_number = Column(String, nullable=False)
```
## Project Structure

```python
.
├── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── database.py
│   ├── redis_client.py
│   └── crud.py
├── streamlit_app.py
├── requirements.txt
└── README.md
```

## Installation

# 1. Clone the repository

```python
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

# 2. Create a virtual environment

```python
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

# 3. Install dependencies
```python
pip install -r requirements.txt
```

## Running the Application

# Start FastAPI Backend
```python
uvicorn app.main:app --reload

API will be available at:
http://127.0.0.1:8000

Swagger UI:
http://127.0.0.1:8000/docs
```

# Start Redis (Optional but Recommended)
```python
redis-server
```

# Start Streamlit Frontend
```python
streamlit run streamlit_app.py

Frontend will be available at:
http://localhost:8501
```

## Future Improvements

- Authentication & Authorization
- Pagination & filtering
- Docker support
- Deployment configuration
- Unit testing
