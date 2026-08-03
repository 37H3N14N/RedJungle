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


@app.post("/member/group/{action}")
def manage_group_member(action, data: dict):
    
    if action == 'create':
        http_response = {
            "endpoint": 'create group member',
            "echo_data": data
        }
        return  http_response 

    if action == 'update':
        http_response = {
            "endpoint": 'update group member',
            "echo_data": data
        }
        return  http_response 

    if action == 'delete':
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


@app.post("/member/super/{action}")
def manage_super_member(action, data: dict):
    
    if action == 'create':
        http_response = {
            "endpoint": 'create super member ',
            "echo_data": data
        }
        return  http_response 

    if action == 'update':
        http_response = {
            "endpoint": 'update super member ',
            "echo_data": data
        }
        return  http_response 

    if action == 'delete':
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


@app.post("/member/folder/{action}")
def manage_folder_member(action, data: dict):
    
    if action == 'create':
        http_response = {
            "endpoint": 'create folder member',
            "echo_data": data
        }
        return  http_response 

    if action == 'update':
        http_response = {
            "endpoint": 'update folder member',
            "echo_data": data
        }
        return  http_response 

    if action == 'delete':
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


@app.post("/member/note/{action}")
def manage_note_member(action, data: dict):
    
    if action == 'create':
        http_response = {
            "endpoint": 'create note member',
            "echo_data": data
        }
        return  http_response 

    if action == 'update':
        http_response = {
            "endpoint": 'update note member',
            "echo_data": data
        }
        return  http_response 

    if action == 'delete':
        http_response = {
            "endpoint": 'delete note member',
            "echo_data": data
        }
        return  http_response 


