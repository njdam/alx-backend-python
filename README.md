# Python Backend

## Introduction

This project is a Python backend application designed to handle various tasks such as user authentication, data processing, and serving API endpoints. It utilizes Flask as the web framework and SQLAlchemy as the ORM (Object-Relational Mapping) tool to interact with the database.


## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/python-backend.git
```

2. Navigate to the project directory:

```bash
cd python-backend
```

3. Create a virtual environment (optional but recommended):

```bash
python3 -m venv venv
```

4. Activate the virtual environment:

* On Linux/macOS:

```bash
source venv/bin/activate
```

* On Windows:

```bash
.\venv\Scripts\activate
```

5. Install dependencies:

```bash
pip install -r requirements.txt
```


## Configuration

Before running the application, you need to set up the configuration file:

1. Create a copy of the example configuration file:

```bash
cp config.example.py config.py
```

2. Update the configuration settings in config.py according to your environment.


## Database Setup

This project uses SQLite as the default database. You can create the necessary database tables by running the following command:

```bash
python manage.py db upgrade
```


## Running the Application

To start the Flask development server, use the following command:

```bash
python manage.py runserver
```
By default, the application will be accessible at http://localhost:5000.

## Testing

To run the tests for this application, execute the following command:

```bash
python manage.py test
```


## API Documentation

The API endpoints and their usage are documented in the API Documentation file.


## License
This project is licensed under the ALX_AFRICA License.
