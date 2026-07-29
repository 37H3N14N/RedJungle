from pydantic import BaseModel

class User_Object(BaseModel):
    user_id: str
    tenant_id: str
    role_id: str
    updated_at: str
    created_at: str
    profiles: list

class Profile_Object(BaseModel):
    profile_id: str
    profile_picture_url: str 
    first_name: str
    last_name: str
    email: str
    users: list


class Send_Log_Data(BaseModel):
    source_service: str
    service_uri: str
    action_crud: str
    user_id: str
    tenant_id: str
    details: dict


class Incoming_Data(BaseModel):
    server_authorization_token: str
    payload: dict






