from  fastapi import FastAPI
from models.room_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()
#####################################################################


@app.get("/member/group/{param_a}")
def get_group_member(param_a, data: Incoming_Data):

    if param_a == 'all':
        http_response = {
            "endpoint": 'get all groups',
            "echo_data": data
        }
        return  http_response 

    if param_a == None:
        http_response = {
            "endpoint": 'get single group',
            "echo_data": data
        }
        return  http_response 


@app.post("/member/group/{param_a}")
def manage_group_member(param_a, data: Incoming_Data):
    
    if param_a == 'create':
        http_response = {
            "endpoint": 'create group',
            "echo_data": data
        }
        return  http_response 

    if param_a == 'update':
        http_response = {
            "endpoint": 'update group',
            "echo_data": data
        }
        return  http_response 

    if param_a == 'delete':
        http_response = {
            "endpoint": 'delete group',
            "echo_data": data
        }
        return  http_response 


@app.get("/member/super/{param_a}")
def get_super_member(param_a, data: Incoming_Data):

    if param_a == 'all':
        http_response = {
            "endpoint": 'get all folders',
            "echo_data": data
        }
        return  http_response 

    if param_a == None:
        http_response = {
            "endpoint": 'get single folder',
            "echo_data": data
        }
        return  http_response 


@app.post("/member/super/{param_a}")
def manage_super_member(param_a, data: Incoming_Data):
    
    if param_a == 'create':
        http_response = {
            "endpoint": 'create folder',
            "echo_data": data
        }
        return  http_response 

    if param_a == 'update':
        http_response = {
            "endpoint": 'update folder',
            "echo_data": data
        }
        return  http_response 

    if param_a == 'delete':
        http_response = {
            "endpoint": 'delete folder',
            "echo_data": data
        }
        return  http_response 



@app.get("/member/folder/{param_a}")
def get_folder_member(param_a, data: Incoming_Data):

    if param_a == 'all':
        http_response = {
            "endpoint": 'get all folders',
            "echo_data": data
        }
        return  http_response 

    if param_a == None:
        http_response = {
            "endpoint": 'get single folder',
            "echo_data": data
        }
        return  http_response 


@app.post("/member/folder/{param_a}")
def manage_folder_member(param_a, data: Incoming_Data):
    
    if param_a == 'create':
        http_response = {
            "endpoint": 'create folder',
            "echo_data": data
        }
        return  http_response 

    if param_a == 'update':
        http_response = {
            "endpoint": 'update folder',
            "echo_data": data
        }
        return  http_response 

    if param_a == 'delete':
        http_response = {
            "endpoint": 'delete folder',
            "echo_data": data
        }
        return  http_response 



@app.get("/member/note/{param_a}")
def get_note_member(param_a, data: Incoming_Data):

    if param_a == 'all':
        http_response = {
            "endpoint": 'get all folders',
            "echo_data": data
        }
        return  http_response 

    if param_a == None:
        http_response = {
            "endpoint": 'get single folder',
            "echo_data": data
        }
        return  http_response 


@app.post("/member/note/{param_a}")
def manage_note_member(param_a, data: Incoming_Data):
    
    if param_a == 'create':
        http_response = {
            "endpoint": 'create folder',
            "echo_data": data
        }
        return  http_response 

    if param_a == 'update':
        http_response = {
            "endpoint": 'update folder',
            "echo_data": data
        }
        return  http_response 

    if param_a == 'delete':
        http_response = {
            "endpoint": 'delete folder',
            "echo_data": data
        }
        return  http_response 


