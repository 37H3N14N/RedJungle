from pydantic import BaseModel

class Room_Object(BaseModel):
    room_id: str
    room_name: str
    room_no: str
    hotel_id: str
    status: str
    price: float
    amenities: list


class Picture_Object(BaseModel):
    picture_id: str
    picture_url: str
    date_created: str
    amenities: list


class Amenity_Object(BaseModel):
    amenity_id: str
    amenity_name: str
    amenity_description: str
    max_occupancy: int
    pictures: list


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






