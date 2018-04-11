# django-rest-api: Dreams API

Python REST API using Django Rest Framework exposing CRUD methods via HTTP to store dreams of users.

Dreams item structure:
	Dreams [
		dreams_id = primary key, autoincrement;
    	username = charfield, length=150;
    	dream_date: date_time;
    	is_lucid: boolean;
	]

- Main URL: http://localhost:8000/api/
- API documentation: http://localhost:8000/api/docs/

- API Methods:
	- Create/Add (POST): create new dream and add it to the dreams list
		- POST http://localhost:8000/api/dreams/ username=some_username dreams_date=some_date is_lucid=true_or_false
	- Retrieve/Get (GET):
		- Get full list of dreams: http://localhost:8000/api/dreams/
		- Get details of dream with dream_id=N: http://localhost:8000/api/dreams/N/
	- Update (PUT): modify values of dream item with dream_id=N
		- PUT http://localhost:8000/api/dreams/N/ username=some_username dreams_date=some_date is_lucid=true_or_false
	- Delete (DELETE): delete dream item with dream_id=N
		- DELETE http://localhost:8000/api/dreams/N/ 
 