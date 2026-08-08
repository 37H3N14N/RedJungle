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



@app.post("/user/")
def manage_user(data: dict):

    allowed_actions = ['create','update','delete']

    if data['action'] not in allowed_actions:
        return 'Page is non existant'
    
    
    if data['action'] == 'create':
        http_response = {
            "endpoint": 'create user',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'update':
        http_response = {
            "endpoint": 'update user',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'delete':
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



@app.post("/session/")
def manage_session(data: dict):
    
    allowed_actions = ['create','update','delete']

    if data['action'] not in allowed_actions:
        return 'Page is non existant'
    
    
    if data['action'] == 'create':
        http_response = {
            "endpoint": 'create session',
            "echo_data": data
        }
        return  http_response 


    if data['action'] == 'delete':
        http_response = {
            "endpoint": 'delete session',
            "echo_data": data
        }
        return  http_response 
















