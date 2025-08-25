# Arithmetic Operations API 
- ---
## Overview 
This API performs basic arithmetic operations: addition, subtraction, multiplication, and division. It’s built with FastAPI and documented using Swagger UI for easy testing and integration. 
- --- 
##  Features 
- `POST /add` – Add two numbers 
- `POST /sub` – Subtract one number from another 
- `POST /mul` – Multiply two numbers 
- `POST /did` – Divide one number by another Each endpoint accepts two numbers in the request body and returns the result in JSON format. 
- ---
##  Technologies Used 
- fastapi
- uvicorn
- pydantic
- pytest
 - ---
## Usage Examples 
### Add Two Numbers 
```http 
POST /add 
Content-Type: application/json 

{ "int1": 10, 
"int2": 5 } 
``` 
**Response:** 
```
json { "result": 15 } 
``` 
- --- 

### Subtract 
```
http 
POST /sub 
Content-Type: application/json 

{ "int1": 10, 
"int2": 5 } 

``` 
**Response:** 
```
json { "result": 5 } 
``` 

- --- 

### Multiply 
```
http 
POST /mil 
Content-Type: application/json 

{ "int1": 10, 
"int2": 5 } 

``` 
**Response:** 
```
json { "result": 50 } 
``` 

- --- 

### Divide 
```
http 
POST /did Content-Type: application/json 

{ "int1": 10, 
"int2": 5 } 

```
**Response:** 
```
json { "result": 2.0 } 
``` 

- --- 

## Testing Unit tests are written using `pytest` and cover all arithmetic functions.
```
bash pytest test_math_functions.py 
``` 
--- -
## Swagger UI Once the server is running, visit: 
``` 
http://localhost:8000/docs 
``` 
Use the Swagger interface to test endpoints, view request schemas, and inspect responses.