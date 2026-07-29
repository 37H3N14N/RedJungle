from model import Incoming_Data
from model import Delete_Data
from  fastapi import FastAPI
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()
#####################################################################

@app.get("/group/{param_a}")
def get_group(param_a, data: Incoming_Data):

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


@app.post("/group/{param_a}")
def manage_group(param_a, data: Incoming_Data):
    
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


@app.get("/folder/{param_a}")
def get_folder(param_a, data: Incoming_Data):

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


@app.post("/folder/{param_a}")
def manage_folder(param_a, data: Incoming_Data):
    
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



@app.get("/note/{param_a}")
def get_folder(param_a, data: Incoming_Data):

    if param_a == 'all':
        http_response = {
            "endpoint": 'get all notes',
            "echo_data": data
        }
        return  http_response 

    if param_a == None:
        http_response = {
            "endpoint": 'get single note',
            "echo_data": data
        }
        return  http_response 


@app.post("/note/{param_a}")
def manage_folder(param_a, data: Incoming_Data):
    
    if param_a == 'create':
        http_response = {
            "endpoint": 'create note',
            "echo_data": data
        }
        return  http_response 

    if param_a == 'update':
        # Route to the note micro service
        http_response = {
            "endpoint": 'update note route',
            "echo_data": data
        }
        return  http_response 

    if param_a == 'delete':
        http_response = {
            "endpoint": 'delete note',
            "echo_data": data
        }
        return  http_response 







