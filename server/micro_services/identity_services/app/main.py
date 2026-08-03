from fastapi import FastAPI
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()
#####################################################################


@app.get("/user/")
def get_user(selection_type: str = 'all',session_id: str = ''):

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single user',
        }
        return  http_response 

    http_response = {
        "endpoint": 'get all users',
    }
    return  http_response 



@app.post("/user/{action}")
def manage_user(action, data: dict):
    
    if action == 'create':
        http_response = {
            "endpoint": 'create user',
            "echo_data": data
        }
        return  http_response 

    if action == 'update':
        http_response = {
            "endpoint": 'update user',
            "echo_data": data
        }
        return  http_response 

    if action == 'delete':
        http_response = {
            "endpoint": 'delete user',
            "echo_data": data
        }
        return  http_response 




@app.get("/session/")
def get_session(selection_type: str = 'all',session_id: str = ''):

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single session',
        }
        return  http_response 

    http_response = {
        "endpoint": 'get all sessions',
    }
    return  http_response 



@app.post("/session/{action}")
def manage_session(action, data: dict):
    
    if action == 'create':
        http_response = {
            "endpoint": 'create session',
            "echo_data": data
        }
        return  http_response 


    if action == 'delete':
        http_response = {
            "endpoint": 'delete session',
            "echo_data": data
        }
        return  http_response 
















