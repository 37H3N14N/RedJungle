from  fastapi import FastAPI
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()
#####################################################################


@app.get("/note-data/")
def get_group_member(selection_type: str = 'all',session_id: str = ''):

    if selection_type == 'single':
        http_response = {
            "endpoint": 'get single note-data',
        }
        return  http_response 

    http_response = {
        "endpoint": 'get all note-datas',
    }
    return  http_response 


@app.post("/note-data/{action}")
def manage_group_member(action, data: dict):
    
    if action == 'create':
        http_response = {
            "endpoint": 'create note',
            "data_pack": data
        }
        return  http_response 

    if action == 'update':
        http_response = {
            "endpoint": 'update note',
            "data_pack": data
        }
        return  http_response 

    if action == 'delete':
        http_response = {
            "endpoint": 'delete note',
            "data_pack": data
        }
        return  http_response 















































