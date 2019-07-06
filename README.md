## Django & Bootstrap Full Dashboard Template Project

This is a base template project for an admin dashboard website, using Django 2 and Admin-LTE.

COURTESY TO ADMIN-LTE FOR THE ENTIRE USER INTERFACE TEMPLATE: https://adminlte.io/

By following a few easy steps, you can get a project up and running quickly, with a fully-configured Django back-end
and a Bootstrap front-end using a beautiful dashboard template. 

The back-end is configured for a local development environment. Using the Django framework, you can 
use this template as a base and then continue working on it for your needs. This template simplifies setting
up a back-end and front-end so that you can quickly get started on your actual project. 

User authentication is fully configured, including login & sign up pages, without the "username"
field that Django User models have originally. 

### Pre-reqs
- Python 3
- Python `venv` module: https://docs.python.org/3/library/venv.html 

```
pip3 install virtualenv
```

### Installation Instructions
Get the repo:
```
git clone https://github.com/AreebaAziz/template_project.git
cd template_project
```

Set up a virtual environment:
```
mkdir env
python3 -m venv env
env/bin/activate
```

Install modules:
```
pip install -r requirements.txt
cd frontend
npm install admin-lte --save
cd ..
```

Create database and superuser:
```
python manage.py migrate
python manage.py createsuperuser
```

Run server:
```
python manage.py runserver
```

Run interactive shell:
```
python manage.py shell_plus
```

### Notes
- on template_project/settings.py, modify database config settings, app name and other config as needed.
- frontend/templates/base_dashboard.html has everything set up for the dashboard pages. To create a new dashboard
page, all you need to do is create a new html file, and write `{% extends 'base_dashboard.html' %}` and 
`{% load static %}` at the top of the file and then enclose all new content in `{% block content %}{% endblock %} `.
