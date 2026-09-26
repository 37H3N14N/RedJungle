from  fastapi import FastAPI, HTTPException, Query
import httpx
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()
#####################################################################

# --------------------------------------------------------------------

@app.get("/content/")
def get_group_member(selection_type: str = 'all',session_id: str = ''):

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single content',
        }
        return  http_response 

    http_response = {
        "endpoint": 'get all contents',
    }
    return  http_response 

# --------------------------------------------------------------------

@app.post("/content/")
def manage_group_member(data: dict):

    allowed_actions = ['create','update','delete']

    if data['action'] not in allowed_actions:
        return 'Page is non existant'

    
    if data['action'] == 'create':
        http_response = {
            "endpoint": 'create note',
            "data_pack": data
        }
        return  http_response 

    if data['action'] == 'update':
        http_response = {
            "endpoint": 'update note',
            "data_pack": data
        }
        return  http_response 

    if data['action'] == 'delete':
        http_response = {
            "endpoint": 'delete note',
            "data_pack": data
        }
        return  http_response 

# --------------------------------------------------------------------

@app.get("/hidden/")
def get_hidden_endpoint():

    http_response = {
        "endpoint": 'get all data from hidden endpoint'
    }
    return  http_response 

# --------------------------------------------------------------------



