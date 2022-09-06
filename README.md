# Deploy a Python (Django) app to Azure with Managed Identity 

This Python app is a simple restaurant review application built with the [Django](https://www.djangoproject.com/) framework. The app uses stores application data in PostgreSQL with environment variables defining the connection info.

This sample app can be run locally and then deployed to Azure. In this repo, the web app is containerized so that it can be run as a container in App Service or Azure Containers Apps. 

If you need an Azure account, you can [create on for free](https://azure.microsoft.com/free/).

A Flask sample application with similar functionality is at https://github.com/Azure-Samples/msdocs-flask-web-app-managed-identity.

## Requirements

The [requirements.txt](./requirements.txt) has the following packages:

| Package | Description |
| ------- | ----------- |
| [Django](https://pypi.org/project/Django/) | Web application framework. |
| [pyscopg2-binary](https://pypi.org/project/psycopg-binary/) | PostgreSQL database adapter for Python. |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Read key-value pairs from .env file and set them as environment variables. In this sample app, environment variables describe how to connect to the database and storage resources. Because managed identity is used no sensitive information is included in environment variables. <br><br> This package is used in the [manage.py](./manage.py) file to load environment variables. |
| [whitenoise](https://pypi.org/project/whitenoise/) | Static file serving for WSGI applications, used in the deployed app. <br><br> This package is used in the [azureproject/production.py](./azureproject/production.py) file, which configures production settings. |

