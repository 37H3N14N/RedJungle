from  fastapi import FastAPI
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()
#####################################################################

# --------------------------------------------------------------------

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


# --------------------------------------------------------------------

@app.post("/group/")
def manage_group(data: dict):

    allowed_actions = ['create','update','delete']

    if data['action'] not in allowed_actions:
        return 'Page is non existant'

    
    if data['action'] == 'create':
        http_response = {
            "endpoint": 'create group',
            'data' : data
        }
        return  http_response 

    if data['action'] == 'update':
        http_response = {
            "endpoint": 'update group',
            'data' : data
        }
        return  http_response 

    if data['action'] == 'delete':
        http_response = {
            "endpoint": 'delete group',
            'data' : data
        }
        return  http_response 


# --------------------------------------------------------------------

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

# --------------------------------------------------------------------

@app.post("/folder/")
def manage_folder(data: str):

    allowed_actions = ['create','update','delete']

    if data['action'] not in allowed_actions:
        return 'Page is non existant'

    
    if data['action'] == 'create':
        http_response = {
            "endpoint": 'create folder',
            'data' : data
        }
        return  http_response 

    if data['action'] == 'update':
        http_response = {
            "endpoint": 'update folder',
            'data' : data
        }
        return  http_response 

    if data['action'] == 'delete':
        http_response = {
            "endpoint": 'delete folder',
            'data' : data
        }
        return  http_response 


# --------------------------------------------------------------------

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


# --------------------------------------------------------------------

@app.post("/note/")
def manage_note(data: str):

    allowed_actions = ['create','update','delete']

    if data['action'] not in allowed_actions:
        return 'Page is non existant'
    

    if data['action'] == 'create':
        http_response = {
            "endpoint": 'create note',
            'data' : data
        }
        return  http_response 

    if data['action'] == 'update':
        http_response = {
            "endpoint": 'update note route',
            'data' : data
        }
        return  http_response 

    if data['action'] == 'delete':
        http_response = {
            "endpoint": 'delete note',
            'data' : data
        }
        return  http_response 


# --------------------------------------------------------------------





