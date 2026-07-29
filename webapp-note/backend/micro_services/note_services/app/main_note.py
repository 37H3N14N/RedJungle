from  fastapi import FastAPI
from models.review_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()
#####################################################################


@app.get("/note/{param_a}")
def get_group_member(param_a, data: Incoming_Data):

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
def manage_group_member(param_a, data: Incoming_Data):
    
    if param_a == 'create':
        http_response = {
            "endpoint": 'create note',
            "echo_data": data
        }
        return  http_response 

    if param_a == 'update':
        http_response = {
            "endpoint": 'update note',
            "echo_data": data
        }
        return  http_response 

    if param_a == 'delete':
        http_response = {
            "endpoint": 'delete note',
            "echo_data": data
        }
        return  http_response 















































