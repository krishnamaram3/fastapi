# Title
This project is intended to touch and feel FastAPI framework.

# Execution Flow
* Step 1: Clone repo
```
git clone https://github.com/krishnamaram3/fastapi.git && cd fastapi
```
* Step 2: Install dependencies
```
pip3 install -r requirements.txt
```
* Step 3: Export environment variables
```
export DB_SERVER="localhost"
export DB_USR="cloud"
export DB_PWD="Cloud@123"
```
* Step 3: To run the server
```
uvicorn main:app --reload
```
* Step 5: Swagger URL for Testing
```
http://127.0.0.1:8000/csp/api/docs
```
