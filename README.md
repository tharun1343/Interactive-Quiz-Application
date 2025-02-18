# Interactive Quiz Application

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

This project is licensed under the MIT License.
