from pydantic import BaseModel


class Incoming_Payload(BaseModel):
    amount_data: str 
    hotel_name: str 
    services:list







