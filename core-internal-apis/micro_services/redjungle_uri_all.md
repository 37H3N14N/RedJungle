=> PRELIMINARY CORRECTION

[substitute every get request to post request]
[the uri will be "/get/old_uri" ,i.e "/get/role"]


###### orchestrator_services_uri ###### 

- /client [post] => external client side ip
- /internal [post] => internal server ip

###### access_control_services_uri ###### *
orchestration server ip only accepted

- /role [crud] 
=>[post,put,delete] = super_admin
=>[get] = anyone / super admin

- /policy [crud] = super_admin
- /decision-log [get,delete] = super_admin / admin

###### auth_services_uri ###### 
orchestration server ip only accepted

- /auth/credential [crud] 
=>[post] = anyone
=>[get] = user / super_admin
=>[put] = user
=>[delete] = user / super_admin

- /auth/session [get,delete] 
=>[get] = anyone / super_admin 
=>[delete] = user / super_admin

- /auth/reset-token [get,delete] 
=>[get] = user / super_admin
=>[delete] = user

###### booking_services_uri ###### 
orchestration server ip only accepted

- /guest [get,post,delete] 
=>[get] = admin / user / super_admin 
=>[post] = user
=>[delete] = guest / admin

- /booking [get,post,delete] 
=>[get] = guest / admin /super_admin
=>[post] = guest
=>[delete] = guest 

- /invoice [get,post,delete] 
=>[get] = guest / admin / super_admin
=>[post] = guest
=>[delete] = guest / admin / super_admin

###### hotel_services_uri ###### 
orchestration server ip only accepted

- /hotel [crud] 
=>[get] = anyone / super_admin 
=>[post] = super_admin 
=>[put] = admin 
=>[delete] = super_admin 

- /hotel-service [crud] 
=> [get] = anyone / super_admin
=> [post] = super_admin
=> [put] = admin 
=> [delete] = super_admin

- /booking-service [crd] 
=> [get] = guest / super admin / admin
=> [post] = guest / super admin
=> [delete] = guest / super admin

- /config [get]  = anyone
- /config [post,put,delete]  = super_admin

###### payment_gateway_services_uri ###### 
orchestration server ip only accepted

- /transaction [get,post,delete] 
=>[get] = user / super admin
=>[post] = user
=>[delete] => user 

- /bank [crud] 
=>[get] = user / super_admin
=>[post] = super_admin
=>[put] = user
=>[delete] = user / super_admin

###### review_services_uri ###### 
orchestration server ip only accepted

- /review [crud] 
=>[get] = anyone 
=>[post] = guest 
=>[put] = guest
=>[delete] = guest /admin / super_admin

###### room_services_uri ###### 
orchestration server ip only accepted

- /room [crud] 
=>[get] = anyone / admin / super_admin
=>[post] = admin 
=>[put] = admin 
=>[delete] = admin  / super_admin 

- /amenity [crud] 
=>[get] = anyone / admin / super_admin
=>[post] = admin 
=>[put] = admin 
=>[delete] = admin  / super_admin 

- /amenity/picture [get,post,delete] 
=>[get] = anyone
=>[post] = admin
=>[delete] = admin / super_user

###### tenant_services_uri ###### 
orchestration server ip only accepted

- /tenant [crud] 
=>[get] = super_admin / platform
=>[post] = super_admin 
=>[put] = super_admin 
=>[delete] = super_admin / platform

- /billing [get,post,delete] 
=>[get] = super_admin / platform
=>[post] = super_admin
=>[delete] = super_admin / platform

###### user_services_uri ###### 
orchestration server ip only accepted

- /user [crud] 
=>[get] = user / super_admin / platform
=>[post] = user
=>[put] = user 
=>[delete] = user 


- /user/profile [crud] 
=>[get] = user / super_admin / platform
=>[post] = user
=>[put] = user 
=>[delete] = user 

###### analytics_services_uri ###### 
orchestration server ip only accepted

- /analytic/event-log [get,post,delete] 
=>[get] = admin / super_admin 
=>[post] = anyone
=>[delete] = admin / super_admin 

- /analytic/metric [get,put,delete] 
=>[get] = admin / super_admin 
=>[put] = admin / super_admin
=>[delete] = admin / super_admin 









