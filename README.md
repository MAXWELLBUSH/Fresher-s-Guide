# 🎓 Fresher's Guide

> A Django-based web platform designed to help first-year university students easily navigate campus life.

---

## 📝 Project Overview

**Fresher's Guide** is a campus navigation and support system that assists first-year students in adapting to university life.  
It provides access to essential information such as **hostels**, **FAQs**, **campus services**, **locations**, and **student profiles**.  
The platform centralizes everything a fresher might need — from accommodation details to service contacts — all in one place.

---

## 🚀 Key Features

### 👤 Users App (Django REST Framework)
- User registration and authentication  
- JWT-based secure login  
- Manage student profiles through REST API  

### 🏫 Hostels App
- View available hostels and their details  
- Hostel descriptions, locations, and amenities  

### ❓ FAQ App
- Common questions for new students  
- Organized by topic (academic, social, administrative)  

### 🗺️ Locations App
- Key campus buildings and their locations  
- Includes directions and short descriptions  

### 🧰 Services App
- List of essential student services (health, IT, transport, etc.)  
- Contact info and operating hours  

---

## 🧩 Tech Stack

| Component | Technology Used |
|------------|-----------------|
| **Backend** | Django, Django REST Framework |
| **Database** | SQLite / PostgreSQL |
| **Frontend** | HTML, CSS, JavaScript |
| **Authentication** | Django REST Framework Auth / JWT |
| **API Testing** | Postman |
| **Version Control** | Git & GitHub |

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

```bash
# Clone the repository
git clone https://github.com/yourusername/freshers-guide.git
cd freshers-guide

# Create a virtual environment
python -m venv venv
# Activate the environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run database migrations
python manage.py makemigrations
python manage.py migrate

# Start the development server
python manage.py runserver
