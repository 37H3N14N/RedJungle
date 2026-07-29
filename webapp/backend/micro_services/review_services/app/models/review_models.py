from pydantic import BaseModel

class Review_Object(BaseModel):
    review_id: str
    user_id: str
    tenant_id: str
    date_created: str
    date_updated: str
    pictures: list
    messages: list


class Picture_Object(BaseModel):
    picture_id: str
    picture_url: str
    date_created: str
    reviews:list


class Message_Object(BaseModel):
    message_id: str
    message_text: str
    date_created: str
    date_updated: str
    reviews:list


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






