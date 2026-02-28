# 🚀 Python OOP & System Design Project

A structured Python project demonstrating Object-Oriented Programming
(OOP), file handling, JSON persistence, modular architecture,
authentication, and CRUD operations.

------------------------------------------------------------------------

## 📌 Overview

This project was built as part of hands-on practice to strengthen core
backend programming concepts using pure Python.

### It includes:

-   Custom Queue Implementation
-   Named Queue with Persistence
-   Authentication System
-   Project Management (CRUD)
-   JSON File Storage
-   Custom Exceptions
-   Clean Modular Structure

------------------------------------------------------------------------

## 🏗️ Project Structure

    project-root/
    │
    ├── basic_queue.py
    ├── namedQueue.py
    ├── main.py
    ├── auth/
    │   ├── user.py
    │   ├── auth_system.py
    │
    ├── projects/
    │   ├── project.py
    │   ├── project_manager.py
    │
    ├── data/
    │   ├── users.json
    │   ├── projects.json
    │   ├── queues.json
    │
    └── README.md

------------------------------------------------------------------------

## 🧠 Concepts Covered

### 🔹 Object-Oriented Programming

-   Classes & Objects
-   Class Methods
-   Encapsulation
-   Custom Exceptions

### 🔹 Data Structures

-   Basic Queue (FIFO)
-   Named Queue with size limitation
-   Centralized queue registry

### 🔹 File Handling

-   JSON serialization
-   Saving and loading system state
-   Persistent storage

### 🔹 Authentication System

-   User registration
-   Login validation
-   Data persistence

### 🔹 Project Management

-   Create project
-   View projects
-   Edit project
-   Delete project

------------------------------------------------------------------------

## 📦 Features

### 1️⃣ Basic Queue

``` python
q = Queue()
q.insert(10)
q.insert(20)
print(q.pop())
```

### 2️⃣ Named Queue (Size Controlled)

``` python
aq = NamedQueue("Orders", 3)
aq.insert(1)
aq.insert(2)
NamedQueue.save()
```

✔️ Raises `QueueOutOfRangeException` when full\
✔️ Can save and reload queues from JSON

------------------------------------------------------------------------

## 💾 Data Persistence

All system data is stored in JSON files:

-   users.json
-   projects.json
-   queues.json

This ensures: - State recovery - Clean separation between logic and
storage - Scalability potential

------------------------------------------------------------------------

## ⚙️ How to Run

``` bash
python main.py
```

Make sure Python 3.8+ is installed.

------------------------------------------------------------------------

## 🎯 Design Goals

-   Clean modular architecture\
-   Separation of concerns\
-   Reusable components\
-   Production-style structure\
-   Clear naming conventions

------------------------------------------------------------------------

## 🔥 Future Improvements

-   Convert Queue to Circular Queue
-   Add password hashing
-   Add logging system
-   Add REST API layer (Flask / FastAPI)
-   Unit testing with pytest
-   Docker support

------------------------------------------------------------------------

## 👨‍💻 Author

Refaay\
Backend Developer in progress 🚀

------------------------------------------------------------------------

## 📜 License

This project is for educational purposes.
