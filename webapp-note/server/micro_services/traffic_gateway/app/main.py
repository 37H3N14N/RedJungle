from models import Incoming_Data_Internal
from  fastapi import FastAPI, HTTPException
import httpx
import sqlalchemy
import psycopg2
import json

#####################################################################
app = FastAPI()
#####################################################################


@app.get("/")
async def get_homepage(session_id: str = ''):

    internal_server = "http://192.168.1.103:9013/group/"
    
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(internal_server, params={'selection_type':'single','session_id':session_id},timeout=4.0)
            response.raise_for_status() 
            return response.json()
            
        except httpx.HTTPStatusError as exc:
            raise HTTPException(
                status_code=exc.response.status_code, 
                detail=f"External API error: {exc.response.text}"
            )
        except httpx.RequestError:
            raise HTTPException(
                status_code=503, 
                detail="External API is unavailable"
            )

@app.post("/group/{action}")
def manage_group(action, data: dict):
    
    if action == 'create':
        http_response = {
            "endpoint": 'create group',
            'data' : data
        }
        return  http_response 

    if action == 'update':
        http_response = {
            "endpoint": 'update group',
            'data' : data
        }
        return  http_response 

    if action == 'delete':
        http_response = {
            "endpoint": 'delete group',
            'data' : data
        }
        return  http_response 

    if action != 'create' or 'update' or 'delete':
        return 'Page is non existant'






#######################################################################


