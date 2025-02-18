<!--# Interactive Quiz Application

An interactive quiz web application developed during Django training. This application allows users to take quizzes with real-time feedback and dynamic scoring.

## Features

- **User-friendly Interface**: Intuitive design for easy navigation.
- **Django Backend**: Built using the Django framework for robust backend logic.
- **Database Management**: Efficient handling of quiz questions and user responses.
- **Dynamic Scoring**: Real-time feedback to enhance engagement.
- **Secure and Scalable**: Implements best practices for data handling and security.

## Tech Stack

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite / PostgreSQL

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/tharun1343/Interactive-Quiz-Application.git
   cd interactive-quiz-app
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations and run the server:
   ```sh
   python manage.py migrate
   python manage.py runserver
   ```

## Usage

- Open your browser and navigate to `http://127.0.0.1:8000/`
- Start the quiz and get real-time feedback on your answers.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`feature-branch`).
3. Commit your changes.
4. Push to your branch and submit a Pull Request.

## License

This project is licensed under the MIT License. -->


# 📝 Interactive Quiz Application Using Django

A **Django-based quiz application** where users can register, log in, add courses and questions, take quizzes, and view their results. The application follows security best practices to prevent common vulnerabilities like **XSS**, **CSRF**, **SQLi**, and **DoS** attacks.


## ⚡ Features

- **User Authentication**: Register, login, and logout functionality.
- **Admin Features**: Admin users can add courses and questions to the quiz.
- **Quiz Taking**: Users can take quizzes, answer questions, and view results with scores and percentages.
- **Profile Management**: Users can update their profile information.
- **Security**: Includes CSRF protection, input validation, secure session management, and protection against common web vulnerabilities.


## 🛠️ Technologies Used

- **Django**: Python-based web framework for building the application.
- **HTML/CSS**: For frontend rendering and styling.
- **SQLite** (or any RDBMS): For database management.
- **Django Forms**: For handling user inputs securely.
- **Django Authentication**: For user login and registration.
- **Security Headers**: Includes security measures to prevent XSS, CSRF, and SQL injection attacks.



## 📋 Setup Instructions

### 🚀 Prerequisites

- Python 3.x
- Django 3.x or higher

### 🖥️ Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/quiz-application.git
    ```

2. **Navigate to the project directory**:
    ```bash
    cd quiz-application
    ```

3. **Create a virtual environment** (recommended):
    ```bash
    python3 -m venv venv
    ```

4. **Activate the virtual environment**:
    - On **macOS/Linux**:
      ```bash
      source venv/bin/activate
      ```
    - On **Windows**:
      ```bash
      venv\Scripts\activate
      ```

5. **Install the required dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

6. **Apply database migrations**:
    ```bash
    python manage.py migrate
    ```

7. **Create a superuser** to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

8. **Run the development server**:
    ```bash
    python manage.py runserver
    ```

   Your app should now be running at `http://127.0.0.1:8000/`.



## 🔒 Security Features

This project follows **OWASP** security standards to ensure the application is secure. Some of the key security measures include:

- **CSRF Protection**: All form submissions include a CSRF token to protect against Cross-Site Request Forgery attacks.
- **XSS Protection**: Django automatically escapes any user-generated content in templates to prevent Cross-Site Scripting vulnerabilities.
- **SQL Injection Protection**: Django's ORM is used to safely interact with the database and prevent SQL injection.
- **Session Security**: All session cookies are marked as secure, and HTTPS is enforced for communication.
- **Rate Limiting**: Protection against brute-force login attacks (using rate-limiting features in Django or third-party packages).


## 📂 Key Views

### 🏠 Home Page

- Displays all available quizzes.
- Users can select a quiz to take.

### 📝 Register & Login

- **Register**: Allows users to create an account with their credentials.
- **Login**: Allows registered users to log in and access the quiz functionality.

### 👤 Profile Management

- Users can view and update their profile information.

### ➕ Add Course & Add Question (Admin Only)

- Admin users can add new courses and questions to the quiz.

### 🏆 Taking Quizzes

- Users can take a quiz and see their score, correct answers, and percentage after submitting.


## 🗂️ Project Structure



```
quiz-application/
├── basic/
│   ├── migrations/
│   ├── templates/
│   │   ├── addQuiz.html
│   │   ├── addQues.html
│   │   ├── profile.html
│   │   ├── Profile_update.html
│   │   ├── ques.html
│   │   └── result.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   └── views.py
├── db.sqlite3
├── manage.py
├── requirements.txt
└── settings.py
```

## 🔧 Requirements

- **Django 3.x or higher**
- **Python 3.x**

To install the required dependencies, run:
```bash
pip install -r requirements.txt
```
## 📸 Screenshot

![Quiz App Screenshot](assets/screenshot.png)

## 📜 License

This project is licensed under the MIT License.



## 📞 Contact

If you have any questions or feedback, feel free to reach out:

- **Name**: Tharun Prasath V K
- **Email**: mail2tharun.prasath@gmail.com
- **LinkedIn**: [Tharun Prasath](https://www.linkedin.com/in/tharunprasathvk)



Thank you for using this Django Quiz Application! 🙏

