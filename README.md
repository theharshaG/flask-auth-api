# flask-auth-api

Flask Authentication API (Python Project)
## Overview

This project is a REST API-based Authentication System built using Flask. It allows users to register, log in, and access protected routes using JWT (JSON Web Token). Passwords are securely hashed and stored in a SQLite database.

## Features

User registration API
User login API
Password hashing for security
JWT-based authentication
Protected routes using token
SQLite database integration

## Technologies Used

Python
Flask
Flask-SQLAlchemy
Flask-JWT-Extended
Werkzeug Security
SQLite

## Project Structure

flask-auth-api/
│
├── main.py
├── auth.db
└── README.md

## How to Run

install python (VS Code)
Install required libraries:
pip install flask flask_sqlalchemy flask_jwt_extended werkzeug

Run the program: python main.py

## How It Works

The application uses Flask to create REST APIs

User data is stored in SQLite database (auth.db)

During registration:
User sends username and password
Password is hashed using Werkzeug
User is stored in database

## During login:
Credentials are verified
If valid, a JWT token is generated

Protected route (/dashboard):
Requires JWT token in request header
If token is valid, access is granted

## API Endpoints

POST /register → Register new user
POST /login → Login and get token
GET /dashboard → Protected route (requires JWT)

## Future Improvements

Add email verification
Add password reset functionality
Implement role-based access control
Use PostgreSQL or MySQL database
Add frontend interface
Deploy on cloud platform

## Author
Harsha G
Learning Python | Embedded Systems | IoT
