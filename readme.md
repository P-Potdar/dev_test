# DevTest - Django File Upload and Summary Report

## Project Overview

DevTest is a Django-based web application developed as part of a Django intern assignment. It enables users to upload an Excel or CSV file, processes the file to generate a summary report, and sends the summary via email to a specified address. The application is deployed on Heroku for accessibility.

## Features

1. **File Upload**: Allows users to upload Excel (.xlsx) or CSV files.
2. **Data Summary**: Generates insights including:
   - Total entries
   - Average Days Past Due (DPD)
   - Maximum DPD
   - State-wise entry counts
3. **Email Summary**: Sends the generated summary to `tech@themedius.ai`.
4. **Deployment**: Hosted on Heroku for easy access.
5. **Version Control**: Code is managed and hosted on GitHub.

## Prerequisites

- Python 3.x
- Django 4.x
- Gunicorn (for deployment on Heroku)

## Getting Started

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/dev_test.git
cd dev_test

2. Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt


4. Configure Email Settings
In DevTest/settings.py, configure your email settings:


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.your_email_provider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_password'
DEFAULT_FROM_EMAIL = 'your_email@example.com'

5. Run Migrations

python manage.py migrate
6. Run the Development Server

python manage.py runserver


Access the app at http://127.0.0.1:8000/.

Usage
Navigate to the upload page.
Upload an Excel or CSV file.
The app will process the file and display a success message upon sending the summary email.
Deployment on Heroku
Follow these steps to deploy on Heroku:

Create a Procfile in the project root: