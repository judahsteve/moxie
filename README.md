# moxie
The application is a self contained api microservice built in django based on the project criteria

## Installation
Below are the steps required to succesfully run the app
- Have a working installation of python You can download the latest version of python here http://www.python.org/download.
- create the python virtual environment with the python -m venv moxie_env for mac or py venv moxie_env for windows
- start the virtual environment with source moxie_env/bin/activate for mac or source moxie_env/bin/activate.bat for windows
- install django using pip install django
- install djangorestframework using pip install djangorestframework

## Database Installation
- Install psycopg2 using pip: pip install psycopg2-binary
- Install django-postgres using pip: pip install django-postgres

Those are the core dependencies that the project requires to execute. 

## Executing the Project
Once you finish installing these dependencies, simply copy the moxie folderinto your new django virtual environment
- type cd moxie to navigate into the moxie folder
- type python manage.py runserver start the django server and execute the project



## Database Schema
The api has 4 database tables
- Medspa
- Service
- Appointment
- Appointment Service

## API Endpoints
### Medspa

**Retrieves all medspas** 
##### Method Get 
http://127.0.0.1:8000/medspas/



**Retrieves medspa with specified id**
##### Method Get 
http://127.0.0.1:8000/medspas/id/


**Create a new medspa**
##### Method Post 
http://127.0.0.1:8000/medspas/
##### payload
{
    "name":"value",
    "address":"value",
    "phone_number":"value",
    "email":"value"
}

**Update medspa with spcified id**
##### Method Put 
http://127.0.0.1:8000/medspas/id/
##### payload
{
    "name":"value",
    "address":"value",
    "phone_number":"value",
    "email":"value"
}

**Delete medspa with specified id**
##### Method Delete 
http://127.0.0.1:8000/medspas/id/


### Service


**Retrieves all services**
##### Method Get 
http://127.0.0.1:8000/services/

 
**Retrieves all services for medspa with the specified id**
##### Method Get
http://127.0.0.1:8000/services/medspa/id


**Retrieves service with specified id**
##### Method Get 
http://127.0.0.1:8000/services/id/


**Create a new service**
##### Method Post 
http://127.0.0.1:8000/services/
##### payload
{
    "name":"value",
    "description":"value",
    "price":"value",
    "duration:"value",
    "medspa":"value"
}


**Update service with spcified id**
##### Method Put 
http://127.0.0.1:8000/services/id/
##### payload
{
    "name":"value",
    "description":"value",
    "duration:"value",
    "price":"value",
}


**Delete service with specified id**
##### Method Delete 
http://127.0.0.1:8000/service/id/


### Appointment


**Retrieves all appointments**
##### Method Get 
http://127.0.0.1:8000/appointments/


**Retrieves all appointments for with based on their status**
##### Method Get 
http://127.0.0.1:8000/appointments/status/option


*valid status options*
- scheduled
- completed
- cancelled


**Retrieves appointment with specified id**
##### Method Get 
http://127.0.0.1:8000/appointments/id/


**Retrieves appointment with based on start date**
##### Method Get 
http://127.0.0.1:8000/appointments/start-date/YYYY-MM-DD/


*example*


http://127.0.0.1:8000/appointments/start-date/2024-04-29/



**Create a new appointment**
##### Method Post 
http://127.0.0.1:8000/appointments/
##### payload
{
    "medspa": value,
    "services": ["values","values",]
    "start_date": "values",
    "start_time": "values"
}


**Update the status of appointment with spcified id**
##### Method Put 
http://127.0.0.1:8000/appointments/id/
##### payload
{
  "status":"value",
}


**Delete service with specified id**
##### Method Delete 
http://127.0.0.1:8000/service/id/
