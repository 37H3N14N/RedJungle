
############### Micro-services addresses ##########################

- V0  =>  orchestrator_services_url = 'http://redjungle-00.lab:7001'
- V1  =>  auth_services_url = 'http://redjungle-00.lab:7010'
- V2  =>  access_control_services_url = 'http://redjungle-00.lab:7020'
- V3  =>  tenant_services_url = 'http://redjungle-00.lab:7030'
- V4  =>  hotel_services_url = 'http://redjungle-00.lab:7040'
- V5  =>  room_services_url = 'http://redjungle-00.lab:7050'
- V6  =>  payment_gateway_services_url = 'http://redjungle-00.lab:7060'
- V7  =>  booking_services_url = 'http://redjungle-00.lab:7070'
- V8  =>  user_services_url = 'http://redjungle-00.lab:7080'
- V9  =>  analytics_services_url = 'http://redjungle-00.lab:7090'
- V10 =>  review_services_url = 'http://redjungle-00.lab:7005'
- V11 =>  audit_logging_services_url = 'http://redjungle-00.lab:7095'



############### Other Specifications ##########################

- Use of both JWT and Session tokens for acs depending on the client being a signed
in user or a random client by IP 
-


= The check in & check out date are in days of the the year [366]
First the function checks the datetime for the current year , appends the year to the input date , checks the db if that is taken then looks for the check out date if taken it gives you the max you can get  then prefix the year to the number thus the accuracy stays and others cannot get in between dates that are occupied ofcourse by room id. 

















