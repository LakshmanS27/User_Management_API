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

Project Structure
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
