# Recipes API


This is a API REST for recipes, with it is possible to search for existing recipes, creating new ones, updating and deleting them from database. Below it wil be described how to install, run and usage.

## Install

    pip install requirements.txt
    
## Set environment variable 
For directory chosen for clone, set environment variable as:
   
    RECIPES_BASE_DATA_DIR: C:\path\to\recipes_api

## Run the app
On chosen directory:

    python server.py

## Run the tests
On chosen directory:

    coverage run --source ./ -m unittest discover

## Create base database
It is not necessary to create de database file since it is already on folder, but in the case of wanting to create the file recipes.db, use the following command:

    python -m db.create_database

# REST API

The REST API operations can be seen fully documented using the Swagger UI through the following URL:
  
    http://localhost:5000/api/ui
  
The REST API operations are also described below.

## Get full list of recipes

### Request

`GET /recipes`

    curl -X GET --header 'Accept: application/json' 'http://localhost:5000/api/recipes'

### Response

    Response Code
    200
    Response Headers
    {
        "access-control-allow-origin": "*",
        "date": "Tue, 05 Mar 2019 16:26:10 GMT",
        "server": "Werkzeug/0.14.1 Python/3.7.1",
        "content-length": "1578",
        "content-type": "application/json"
    }

## Create a new recipe

### Request

`POST /recipes`

    curl -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ \ 
         "name": "string", \ 
         "ingredients": "string", \ 
         "preparation": "string", \ 
         "servings": 0, \ 
         "total_time": "string", \ 
         "tags": "string" \ 
     }' 'http://localhost:5000/api/recipes'

### Response

    Response Code
    201
    Response Headers
    {
        "access-control-allow-origin": "http://localhost:5000",
        "date": "Wed, 06 Mar 2019 15:16:42 GMT",
        "server": "Werkzeug/0.14.1 Python/3.7.1",
        "content-length": "380",
        "vary": "Origin",
        "content-type": "application/json"
    }

## Get a specific recipe by name

### Request

`GET /recipes/{name}`

    curl -X GET --header 'Accept: application/json' 'http://localhost:5000/api/recipes/Name'

### Response

    Response Code
    200
    Response Headers
    {
        "access-control-allow-origin": "*",
        "date": "Tue, 05 Mar 2019 16:28:16 GMT",
        "server": "Werkzeug/0.14.1 Python/3.7.1",
        "content-length": "498",
        "content-type": "application/json"
    }

## Get a list of recipes containing one specific ingredient   
### Request

`GET /recipes/ingredient/{ingredient}`

    curl -X GET --header 'Accept: application/json' 'http://localhost:5000/api/recipes/ingredient/ingredient''

### Response

    Response Code
    200
    Response Headers
    {
        "access-control-allow-origin": "*",
        "date": "Tue, 05 Mar 2019 16:28:16 GMT",
        "server": "Werkzeug/0.14.1 Python/3.7.1",
        "content-length": "522",
        "content-type": "application/json"
    }
    
## Get a list of recipes containing one specific tag   
### Request

`GET /recipes/tag/{tag}`

    curl -X GET --header 'Accept: application/json' 'http://localhost:5000/api/recipes/tag/tag'


### Response

    Response Code
    200
    Response Headers
    {
        "access-control-allow-origin": "*",
        "date": "Tue, 05 Mar 2019 16:28:16 GMT",
        "server": "Werkzeug/0.14.1 Python/3.7.1",
        "content-length": "404",
        "content-type": "application/json"
    }

## Update a recipe

### Request

`PUT /recipes/{name}`

    curl -X PUT --header 'Content-Type: application/json' --header 'Accept: application/json' -d '{ \ 
    "ingredients": "string", \ 
    "name": "string", \ 
    "preparation": "string", \ 
    "recipe_id": 0, \ 
    "servings": 0, \ 
    "tags": "string", \ 
    "timestamp": "string", \ 
    "total_time": "string" \ 
    }' 'http://localhost:5000/api/recipes/Aqueous%20Martini'
### Response

    Response Code
    200
    Response Headers
    {
        "access-control-allow-origin": "http://localhost:5000",
        "date": "Wed, 06 Mar 2019 16:37:10 GMT",
        "server": "Werkzeug/0.14.1 Python/3.7.1",
        "content-length": "380",
        "vary": "Origin",
        "content-type": "application/json"
    }

## Delete a recipe by name

### Request

`DELETE /recipes/{name}`

    curl -X DELETE --header 'Accept: text/html' 'http://localhost:5000/api/recipes/name'


### Response

    Response Code
    200
    Response Headers
    {
        "access-control-allow-origin": "http://localhost:5000",
        "date": "Wed, 06 Mar 2019 15:14:24 GMT",
        "server": "Werkzeug/0.14.1 Python/3.7.1",
        "content-length": "30",
        "vary": "Origin",
        "content-type": "text/html; charset=utf-8"
    }
