
###################### ADMIN PRIVILAGE #######################
{
"service_authorization":"internal_Service_Call",
"payload":{
    "action": "get",
   "details":{
   "entity_count":"multiple"/"entity_count":"single",
    }
  }
}


#################### NORMAL PRIVILAGE ##########################
{
"service_authorization":"internal_Service_Call",
"payload":{
    "action": "get",
   "details":{
   "user_id": "user_5485",
   "email": "email@there.com"
    }
  }
}

########################### BOOKING API CALL STRUCTURES ###########################

=> create invoice

{
    "server_authorization_token":"server_authorization_token001",
    "payload":{
            "action": "create",
            "details":{
                "booking_id": "booking_5485"
            }
                
        }
}





