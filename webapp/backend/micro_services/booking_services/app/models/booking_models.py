from pydantic import BaseModel

class Booking_Object(BaseModel):
    booking_id: str
    tenant_id: str
    hotel_id: str
    room_id: str
    check_in_date: str
    check_out_date: str
    total_price: float
    payment_transaction_id: str
    created_at: str
    guests: list


class Guest_Object(BaseModel):
    guest_id: str
    user_id: str 
    email: str 
    created_at: str 
    bookings: list


class Invoice_Object(BaseModel):
    invoice_id: str
    booking_id: str
    invoice_number: int
    status: str
    created_at:str


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








