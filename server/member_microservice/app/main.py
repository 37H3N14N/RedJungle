from  fastapi import FastAPI
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()
#####################################################################


@app.get("/member/group/")
def get_group_member(selection_type: str = 'all',session_id: str = ''):

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single group member',
        }
        return  http_response 

    http_response = {
        "endpoint": 'get all group members',
    }
    return  http_response 


@app.post("/member/group/")
def manage_group_member(data: dict):

    allowed_actions = ['create','update','delete']

    if data['action'] not in allowed_actions:
        return 'Page is non existant'
    

    if data['action'] == 'create':
        http_response = {
            "endpoint": 'create group member',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'update':
        http_response = {
            "endpoint": 'update group member',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'delete':
        http_response = {
            "endpoint": 'delete group member',
            "echo_data": data
        }
        return  http_response 


@app.get("/member/super/")
def get_super_member(selection_type: str = 'all',session_id: str = ''):

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single super members',
        }
        return  http_response 

    http_response = {
        "endpoint": 'get all super members',
    }
    return  http_response 


@app.post("/member/super/")
def manage_super_member(data: dict):

    allowed_actions = ['create','update','delete']

    if data['action'] not in allowed_actions:
        return 'Page is non existant'
    
    
    if data['action'] == 'create':
        http_response = {
            "endpoint": 'create super member ',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'update':
        http_response = {
            "endpoint": 'update super member ',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'delete':
        http_response = {
            "endpoint": 'delete super member ',
            "echo_data": data
        }
        return  http_response 



@app.get("/member/folder/")
def get_folder_member(selection_type: str = 'all',session_id: str = ''):

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single folder members',
        }
        return  http_response 

    http_response = {
        "endpoint": 'get all folders members',
    }
    return  http_response 


@app.post("/member/folder/")
def manage_folder_member(data: dict):
    
    allowed_actions = ['create','update','delete']

    if data['action'] not in allowed_actions:
        return 'Page is non existant'
    
    
    if data['action'] == 'create':
        http_response = {
            "endpoint": 'create folder member',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'update':
        http_response = {
            "endpoint": 'update folder member',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'delete':
        http_response = {
            "endpoint": 'delete folder member',
            "echo_data": data
        }
        return  http_response 



@app.get("/member/note/")
def get_note_member(selection_type: str = 'all',session_id: str = ''):

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single note member',
        }
        return  http_response 

    http_response = {
        "endpoint": 'get all note members',
    }
    return  http_response 


@app.post("/member/note/")
def manage_note_member(data: dict):
    
    allowed_actions = ['create','update','delete']

    if data['action'] not in allowed_actions:
        return 'Page is non existant'
    
    
    if data['action'] == 'create':
        http_response = {
            "endpoint": 'create note member',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'update':
        http_response = {
            "endpoint": 'update note member',
            "echo_data": data
        }
        return  http_response 

    if data['action'] == 'delete':
        http_response = {
            "endpoint": 'delete note member',
            "echo_data": data
        }
        return  http_response 


