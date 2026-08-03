from model import Incoming_Payload
from  fastapi import FastAPI
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()
#####################################################################

@app.get("/group/", )
def get_group(selection_type: str = 'all',session_id: str = ''):

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single group',
            'session_id': session_id
        }
        return  http_response 
 
    http_response = {
        "endpoint": 'get all groups',
        'session_id': session_id
    }
    return  http_response 


@app.post("/group/{action}")
def manage_group(action, data: dict):
    
    if action == 'create':
        http_response = {
            "endpoint": 'create group',
            'data' : data
        }
        return  http_response 

    if action == 'update':
        http_response = {
            "endpoint": 'update group',
            'data' : data
        }
        return  http_response 

    if action == 'delete':
        http_response = {
            "endpoint": 'delete group',
            'data' : data
        }
        return  http_response 

    if action != 'create' or 'update' or 'delete':
        return 'Page is non existant'


@app.get("/folder/")
def get_folder(selection_type: str = 'all',session_id: str = ''):

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single folder',
        }
        return  http_response 

    http_response = {
        "endpoint": 'get all folders',
    }
    return  http_response 


@app.post("/folder/{action}")
def manage_folder(action, data: str):
    
    if action == 'create':
        http_response = {
            "endpoint": 'create folder',
        }
        return  http_response 

    if action == 'update':
        http_response = {
            "endpoint": 'update folder',
        }
        return  http_response 

    if action == 'delete':
        http_response = {
            "endpoint": 'delete folder',
        }
        return  http_response 



@app.get("/note/")
def get_note(selection_type: str = 'all',session_id: str = ''):

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single note ',
        }
        return  http_response 

    http_response = {
        "endpoint": 'get all notes',
    }
    return  http_response 


@app.post("/note/{action}")
def manage_note(action, data: str):
    
    if action == 'create':
        http_response = {
            "endpoint": 'create note',
        }
        return  http_response 

    if action == 'update':
        http_response = {
            "endpoint": 'update note route',
        }
        return  http_response 

    if action == 'delete':
        http_response = {
            "endpoint": 'delete note',
        }
        return  http_response 







