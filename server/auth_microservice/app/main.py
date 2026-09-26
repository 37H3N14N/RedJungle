from  fastapi import FastAPI
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()
#####################################################################


@app.get("/auth/group/")
def get_group_auth(selection_type: str = 'all',session_id: str = ''):

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single group auth',
        }
        return  http_response 

    http_response = {
        "endpoint": 'get all group auths',
    }
    return  http_response 


@app.post("/auth/group/")
def manage_group_auth(data: dict):

    allowed_actions = ['create','update','delete']

    if data['action'] not in allowed_actions:
        return 'Page is non existant'
    

    if data['action'] == 'create':
        http_response = {
            "endpoint": 'create group auth',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'update':
        http_response = {
            "endpoint": 'update group auth',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'delete':
        http_response = {
            "endpoint": 'delete group auth',
            "echo_data": data
        }
        return  http_response 


@app.get("/auth/folder/")
def get_folder_auth(selection_type: str = 'all',session_id: str = ''):

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single folder auths',
        }
        return  http_response 

    http_response = {
        "endpoint": 'get all folders auths',
    }
    return  http_response 


@app.post("/auth/folder/")
def manage_folder_auth(data: dict):
    
    allowed_actions = ['create','update','delete']

    if data['action'] not in allowed_actions:
        return 'Page is non existant'
    
    
    if data['action'] == 'create':
        http_response = {
            "endpoint": 'create folder auth',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'update':
        http_response = {
            "endpoint": 'update folder auth',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'delete':
        http_response = {
            "endpoint": 'delete folder auth',
            "echo_data": data
        }
        return  http_response 



@app.get("/auth/note/")
def get_note_auth(selection_type: str = 'all',session_id: str = ''):

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single note auth',
        }
        return  http_response 

    http_response = {
        "endpoint": 'get all note auths',
    }
    return  http_response 


@app.post("/auth/note/")
def manage_note_auth(data: dict):
    
    allowed_actions = ['create','update','delete']

    if data['action'] not in allowed_actions:
        return 'Page is non existant'
    
    
    if data['action'] == 'create':
        http_response = {
            "endpoint": 'create note auth',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'update':
        http_response = {
            "endpoint": 'update note auth',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'delete':
        http_response = {
            "endpoint": 'delete note auth',
            "echo_data": data
        }
        return  http_response 


