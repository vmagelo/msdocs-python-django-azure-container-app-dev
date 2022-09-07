# Deploy a Python (Django) app to Azure with Managed Identity 

This Python app is a simple restaurant review application built with the [Django](https://www.djangoproject.com/) framework. The app uses stores application data in PostgreSQL with environment variables defining the connection info.

This sample app can be run locally and then deployed to Azure. Here are some scenarios:

* You can run the web app locally in a virtual environment. Make sure to define *.env* file with environment settings.

* You can create a container locally and run it in Docker. For this scenario, set REMOTE_POSTGRESQL=1 in *.env* file and use the command: `docker run -it --env-file .env --publish 8000:8000/tcp msdocspythondjangoazurecontainerappdev:latest` set environment variables for container. 

  If you want to use PostgreSQL instance locally, you add `--add-host` to the Docker command. For more information, see the [Docker run](https://docs.docker.com/engine/reference/commandline/run/) command. For an example of how to do this with MongoDB, see [Build and test a containerized Python web app locally](https://docs.microsoft.com/azure/developer/python/tutorial-containerize-deploy-python-web-app-azure-02).

* Deploy the code to App Service. See [Quickstart: Deploy a Python (Django or Flask) web app to Azure App Service](https://docs.microsoft.com/azure/app-service/quickstart-python) and [Overview: Deploy a Python web app to Azure with managed identity](https://docs.microsoft.com/azure/developer/python/tutorial-python-managed-identity-01).

* Create a container from the web app and deploy to Web Apps for Containers (App Service). See [Overview: Containerized Python web app on Azure](https://docs.microsoft.com/azure/developer/python/tutorial-containerize-deploy-python-web-app-azure-01).

* Run the code in Azure Container Apps. **This repo is targeting this scenario.**

If you need an Azure account, you can [create on for free](https://azure.microsoft.com/free/).

A Flask sample application with similar functionality is at **TBD**.

## Requirements

The [requirements.txt](./requirements.txt) has the following packages:

| Package | Description |
| ------- | ----------- |
| [Django](https://pypi.org/project/Django/) | Web application framework. |
| [pyscopg2-binary](https://pypi.org/project/psycopg-binary/) | PostgreSQL database adapter for Python. |
| [gunicorn](https://pypi.org/project/gunicorn/) | WSGI HTTP Server for UNIX. Required for running container in [VS Code](https://code.visualstudio.com/docs/containers/quickstart-python#_gunicorn-modifications-for-djangoflask-apps) and used in deployment Azure. |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Read key-value pairs from .env file and set them as environment variables. In this sample app, environment variables describe how to connect to the database and storage resources. Because managed identity is used no sensitive information is included in environment variables. <br><br> This package is used in the [manage.py](./manage.py) file to load environment variables. |
| [requests](https://pypi.org/project/requests/) | Python HTTP for Humans. |
| [whitenoise](https://pypi.org/project/whitenoise/) | Static file serving for WSGI applications, used in the deployed app. <br><br> This package is used in the [azureproject/production.py](./azureproject/production.py) file, which configures production settings. |

