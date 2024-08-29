# moxie
The application is a self contained api microservice built in django based on the project criteria

## Installtion
Below are the steps required to succesfully run the app
- Have a working installation of python You can download the latest version of python here http://www.python.org/download.
- create the python virtual environment with the python -m venv moxie_env for mac or py venv moxie_env for windows
- start the virtual environment with source moxie_env/bin/activate for mac or source moxie_env/bin/activate.bat for windows
- install django using pip install django
- install djangorestframework using pip install djangorestframework

## Database Installation
- Install psycopg2 using pip: pip install psycopg2-binary
- Install django-postgres using pip: pip install django-postgres

Those are the core dependencies that the project requires to execute

## Database Schema
The api has 4 database tables
- Medspa
- Service
- Appointment
- Appointment Service

## API Endpoints
### Medspa

##### Method Get 
**Retrieves all medspas**
http://127.0.0.1:8000/medspas/

##### Method Get 
**Retrieves medspa with specified id**
http://127.0.0.1:8000/medspas/id/

##### Method Post 
**Create a new medspa**
http://127.0.0.1:8000/medspas/
**payload**
{
    "name":"value",
    "address":"value",
    "phone_number":"value",
    "email":"value"
}

##### Method Put 
**Update medspa with spcified id **
http://127.0.0.1:8000/medspas/id/
**payload**
{
    "name":"value",
    "address":"value",
    "phone_number":"value",
    "email":"value"
}

##### Method Delete 
**Delete medspa with specified id**
http://127.0.0.1:8000/medspas/id/


### Service

##### Method Get 
**Retrieves all services**
http://127.0.0.1:8000/services/

##### Method Get 
**Retrieves all services for medspa with the specified id**
http://127.0.0.1:8000/services/medspa/id

##### Method Get 
**Retrieves service with specified id**
http://127.0.0.1:8000/services/id/

##### Method Post 
**Create a new service**
http://127.0.0.1:8000/services/
**payload**
{
    "name":"value",
    "description":"value",
    "price":"value",
    "duration:"value",
    "medspa":"value"
}

##### Method Put 
**Update service with spcified id **
http://127.0.0.1:8000/services/id/
**payload**
{
    "name":"value",
    "description":"value",
    "duration:"value",
    "price":"value",
}

##### Method Delete 
**Delete service with specified id**
http://127.0.0.1:8000/service/id/


### Appointment

##### Method Get 
**Retrieves all appointments**
http://127.0.0.1:8000/appointments/

##### Method Get 
**Retrieves all appointments for with based on their status**
http://127.0.0.1:8000/appointments/status/option
*valid status options*
- scheduled
- completed
- cancelled

##### Method Get 
**Retrieves appointment with specified id**
http://127.0.0.1:8000/appointments/id/

##### Method Get 
**Retrieves appointment with based on start date**
http://127.0.0.1:8000/appointments/start-date/YYYY-MM-DD/
*example*
http://127.0.0.1:8000/appointments/start-date/2024-04-29/


##### Method Post 
**Create a new appointment**
http://127.0.0.1:8000/appointments/
**payload**
{
    "medspa": value,
    "services": ["values","values",]
    "start_date": "values",
    "start_time": "values"
}

##### Method Put 
**Update the status of appointment with spcified id **
http://127.0.0.1:8000/appointments/id/
**payload**
{
  "status":"value",
}

##### Method Delete 
**Delete service with specified id**
http://127.0.0.1:8000/service/id/
