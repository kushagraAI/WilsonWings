# Travel App

This is a Django-based travel application that allows users to create, update, delete, and view travel destinations. The API is protected by token-based authentication to ensure that only authenticated users can perform certain actions.

## Table of Contents

- [Installation](git clone https://github.com/https://github.com/kushagraAI/WilsonWings.git)
- [Running the Project](python manage.py runserver)
- [Running the Tests](python manage.py test)
- [API Endpoints](http://localhost:8000/destinations/)

### Prerequisites

- Python 3.x
- pip (Python package installer)
- virtualenv (recommended)
- Django (install latest version of Django)
- Django REST Framework (install latest version of Django REST Framework)

### Clone the Repository

```
git clone https://github.com/https://github.com/kushagraAI/WilsonWings.git
```

## Installation

Follow these steps to set up the project on your local machine:

- Activate virtual environment (if not already activated) and install all required dependencies by running `pip install -r requirements.txt` in a terminal window.

##### Activate virtual Environment =

- "venv\Scripts\activate" (for windows users)
- "source venv/bin/activate" (for linux and macOS users)

### Run the Project

- python manage.py runserver

###Set Up the Database

### Run the following commands to set up the database:

- python manage.py makemigrations
- python manage.py migrate

### Create a Superuser

#### Create a superuser account to access the Django admin panel.

- python manage.py createsuperuser

### Running the Tests

To run the tests, use the following command:

- python manage.py test

### API Endpoints

Here are the main API endpoints provided by the application:

### Authentication

- Login: /api-token-auth/ (POST)
  Destinations
- List all destinations: /destinations/ (GET) - NO authentication requires
- Create a new destination: /destinations/ (POST) - Requires authentication
- Retrieve a specific destination: /destinations/<id>/ (GET)
- Update a specific destination: /destinations/<id>/ (PUT) - Requires authentication
- Delete a specific destination: /destinations/<id>/ (DELETE) - Requires authentication

### Postman collections

Soon Be Update here...
