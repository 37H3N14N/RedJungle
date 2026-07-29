from  fastapi import FastAPI
from models.auth_models import Incoming_Data
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()

#####################################################################


@app.post("/get/auth/{param_a}")
def main_get_post(param_a, data: Incoming_Data):

    if param_a == 'credential':
        respond = {
            "endpoint": 'get credential',
            "echo_data": data
        }
        return  respond

    if param_a == 'session':
        respond = {
            "endpoint": 'get session',
            "echo_data": data
        }
        return  respond

    if param_a == 'reset-token':
        respond = {
            "endpoint": 'get password reset token',
            "echo_data": data
        }
        return  respond


@app.post("/auth/{param_a}")
def main_post(param_a, data: Incoming_Data):

    if param_a == 'credential':
        respond = {
            "endpoint": 'post credential',
            "echo_data": data
        }
        return  respond

    if param_a == 'session':
        respond = {
            "endpoint": 'post session',
            "echo_data": data
        }
        return  respond

    if param_a == 'reset-token':
        respond = {
            "endpoint": 'post password reset token',
            "echo_data": data
        }
        return  respond



@app.put("/auth/credential")
def main_put(data: Incoming_Data):
    respond = {
        "endpoint": 'put credential',
        "echo_data": data
    }
    return  respond


@app.delete("/auth/{param_a}")
def main_delete(param_a, data: Incoming_Data):

    if param_a == 'credential':
        respond = {
            "endpoint": 'delete credential',
            "echo_data": data
        }
        return  respond

    if param_a == 'session':
        respond = {
            "endpoint": 'delete session',
            "echo_data": data
        }
        return  respond

    if param_a == 'reset-token':
        respond = {
            "endpoint": 'delete password reset token',
            "echo_data": data
        }
        return  respond







