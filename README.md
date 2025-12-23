# 🎓 Learning Management System (LMS) – Backend API

A role-based Learning Management System (LMS) backend built with **Django** and **Django REST Framework**.
This project is currently **under active development** and focuses on building a scalable, production-ready REST API.

---

## 🚀 Project Status

⚠️ **Work in Progress**

Core authentication, user roles, course, category, and module management APIs are implemented.
Advanced features such as lesson management, enrollments, permissions optimization, and analytics are planned.

---

## 🛠 Tech Stack

* **Backend:** Django, Django REST Framework (DRF)
* **Authentication:** JWT (Simple JWT)
* **API Documentation:** Swagger & Redoc (drf-spectacular)
* **Database:** SQLite (development)
  PostgreSQL (planned for production)
* **Architecture:** Modular, role-based REST API

---

## 👥 User Roles

The system currently supports the following user roles:

* **Student** – Consume courses and learning content
* **Instructor** – Create and manage courses/modules
* **Admin** – Full system control and management

> Role-based permissions are being gradually refined.

---

## 🔐 Authentication & User Management APIs

**Base Path:** `/users/`

| Method | Endpoint                | Description                  |
| ------ | ----------------------- | ---------------------------- |
| POST   | `/users/register/`      | Register a new user          |
| POST   | `/users/send-otp/`      | Send email verification OTP  |
| POST   | `/users/verify-email/`  | Verify email using OTP       |
| POST   | `/users/login/`         | Login and receive JWT tokens |
| POST   | `/users/token/refresh/` | Refresh access token         |
| POST   | `/users/logout/`        | Logout user                  |

---

## 📂 Category Management APIs

**Base Path:** `/`

| Method | Endpoint            | Description               |
| ------ | ------------------- | ------------------------- |
| GET    | `/categories/`      | List all categories       |
| POST   | `/categories/`      | Create a new category     |
| GET    | `/categories/<id>/` | Retrieve category details |
| PUT    | `/categories/<id>/` | Update a category         |
| DELETE | `/categories/<id>/` | Delete a category         |

---

## 📚 Course Management APIs

**Base Path:** `/`

| Method | Endpoint               | Description           |
| ------ | ---------------------- | --------------------- |
| POST   | `/course/create/`      | Create a new course   |
| PUT    | `/course/<id>/update/` | Update course details |
| DELETE | `/course/<id>/delete/` | Delete a course       |

---

## 📦 Module Management APIs

**Base Path:** `/module/`

| Method | Endpoint               | Description                    |
| ------ | ---------------------- | ------------------------------ |
| POST   | `/module/create/`      | Create a module under a course |
| PUT    | `/module/<id>/update/` | Update module details          |
| DELETE | `/module/<id>/delete/` | Delete a module                |

---

## 📑 API Documentation

Interactive API documentation is available:

* **Swagger UI:** `/docs/`
* **Redoc:** `/redoc/`
* **OpenAPI Schema:** `/schema/`

---

## 🧩 Project Structure (Simplified)

```text
StudyFlow-LMS-Backend/
├── courses/
├── modules/
├── users/
├── manage.py
├── requirements.txt
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/asadoojjaman00/StudyFlow-LMS-Backend
cd StudyFlow-LMS-Backend
```

---

### 2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

---

### 3️⃣ Activate Virtual Environment

#### 🪟 Windows

```bash
venv\Scripts\activate
```

#### 🍎 macOS / 🐧 Linux

```bash
source venv/bin/activate
```

---

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 5️⃣ Run Migrations & Start Server

```bash
python manage.py migrate
python manage.py runserver
```

---

## 🔮 Future Improvements (Planned)

* Lesson & content management
* Student enrollment system
* Progress tracking
* Fine-grained role permissions
* PostgreSQL database integration
* Caching & performance optimization
* Unit & integration testing

---

## 👨‍💻 Author

**Asadoojjaman**
Junior Python Backend Developer

* GitHub: [https://github.com/asadoojjaman00](https://github.com/asadoojjaman00)
* LinkedIn: [https://www.linkedin.com/in/asadoojjaman00](https://www.linkedin.com/in/asadoojjaman00)

---

> This project represents my hands-on learning journey in backend development and is continuously evolving.
