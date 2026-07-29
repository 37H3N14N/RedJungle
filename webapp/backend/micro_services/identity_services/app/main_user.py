from  fastapi import FastAPI
from models.user_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
from functions.main_function import create_new_user
from functions.main_function import get_user
from functions.main_function import get_profile

#####################################################################
app = FastAPI()


#####################################################################
@app.post("/get/user")
def main_get_post(data: Incoming_Data):

    response_data = get_user(data)
    return  response_data


#####################################################################
@app.post("/get/user/profile")
def main_get_post(data: Incoming_Data):

    response_data = get_profile(data)
    return  response_data


#####################################################################
@app.post("/user")
def main_post(data: Incoming_Data):

    response_data = create_new_user(data)
    return  response_data


#####################################################################
@app.post("/user/profile")
def main_post(data: Incoming_Data):
    respond = {
        "endpoint": 'post user profile',
        "echo_data": data
    }
    return  respond


#####################################################################
@app.put("/user")
def main_put(data: Incoming_Data):
    respond = {
        "endpoint": 'put user',
        "echo_data": data
    }
    return  respond


#####################################################################
@app.put("/user/profile")
def main_put(data: Incoming_Data):
    respond = {
        "endpoint": 'put user profile',
        "echo_data": data
    }
    return  respond


#####################################################################
@app.delete("/user")
def main_delete(data: Incoming_Data):
    respond = {
        "endpoint": 'delete user',
        "echo_data": data
    }
    return  respond


#####################################################################
@app.delete("/user/profile")
def main_delete(data: Incoming_Data):
    respond = {
        "endpoint": 'delete user profile',
        "echo_data": data
    }
    return  respond


#####################################################################




















