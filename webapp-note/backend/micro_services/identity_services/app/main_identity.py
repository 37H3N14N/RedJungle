from models import Incoming_Data
from fastapi import FastAPI
import sqlalchemy
import psycopg2
import json

#####################################################################
from functions.main_function import create_new_user
from functions.main_function import get_user

#####################################################################
app = FastAPI()
#####################################################################


@app.get("/user/{param_a}")
def get_user(param_a, data: Incoming_Data):

    if param_a == 'all':
        http_response = {
            "endpoint": 'get all users',
            "echo_data": data
        }
        return  http_response 

    if param_a == None:
        http_response = {
            "endpoint": 'get single user',
            "echo_data": data
        }
        return  http_response 


@app.post("/user/{param_a}")
def manage_user(param_a, data: Incoming_Data):
    
    if param_a == 'create':
        http_response = {
            "endpoint": 'create user',
            "echo_data": data
        }
        return  http_response 

    if param_a == 'update':
        http_response = {
            "endpoint": 'update user',
            "echo_data": data
        }
        return  http_response 

    if param_a == 'delete':
        http_response = {
            "endpoint": 'delete user',
            "echo_data": data
        }
        return  http_response 




@app.get("/session/{param_a}")
def get_session(param_a, data: Incoming_Data):

    if param_a == 'all':
        http_response = {
            "endpoint": 'get all sessions',
            "echo_data": data
        }
        return  http_response 

    if param_a == None:
        http_response = {
            "endpoint": 'get single session',
            "echo_data": data
        }
        return  http_response 


@app.post("/session/{param_a}")
def manage_session(param_a, data: Incoming_Data):
    
    if param_a == 'create':
        http_response = {
            "endpoint": 'create session',
            "echo_data": data
        }
        return  http_response 


    if param_a == 'delete':
        http_response = {
            "endpoint": 'delete session',
            "echo_data": data
        }
        return  http_response 
















