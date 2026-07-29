step_object = [
    
#################### ACCESSS CONTROL SERVER #####################

######## CREATE ROLE
# get role 
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$1",
        "relative_url":"/role",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE ROLE
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$2",
        "relative_url":"/role",
        "request_type": 'put',
        "execution_order": 1
    },

######## DELETE ROLE
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$3",
        "relative_url":"/role",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET ROLE
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$4",
        "relative_url":"/get/role",
        "request_type": 'post',
        "execution_order": 1
    },

######## CREATE POLICY
# get policy 
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$5",
        "relative_url":"/policy",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE POLICY
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$6",
        "relative_url":"/policy",
        "request_type": 'put',
        "execution_order": 1
    },

######## DELETE POLICY
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$7",
        "relative_url":"/policy",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET POLICY
    {
        "step_id":"",
        "service_id":"#4",
        "workflow_id":"$8",
        "relative_url":"/get/policy",
        "request_type": 'post',
        "execution_order": 1
    },


#################### HOTEL SERVER #####################

######## CREATE HOTEL
# get_hotel
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$21",
        "relative_url":"/hotel",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE HOTEL
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$22",
        "relative_url":"/hotel",
        "request_type": 'put',
        "execution_order": 1
    },

######## DELETE HOTEL
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$23",
        "relative_url":"/hotel",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET HOTEL
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$24",
        "relative_url":"/get/hotel",
        "request_type": 'post',
        "execution_order": 1
    },

######## CREATE HOTEL SERVICE
# get hotel service
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$25",
        "relative_url":"/hotel-service",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE HOTEL SERVICE
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$26",
        "relative_url":"/hotel-service",
        "request_type": 'put',
        "execution_order": 1
    },

######## DELETE HOTEL SERVICE
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$27",
        "relative_url":"/hotel-service",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET HOTEL SERVICE
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$28",
        "relative_url":"/get/hotel-service",
        "request_type": 'post',
        "execution_order": 1
    },

######## CREATE CONFIG
# get configs
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$29",
        "relative_url":"/config",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE CONFIG
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$30",
        "relative_url":"/config",
        "request_type": 'put',
        "execution_order": 1
    },

######## DELETE CONFIG
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$31",
        "relative_url":"/config",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET CONFIG
    {
        "step_id":"",
        "service_id":"#6",
        "workflow_id":"$32",
        "relative_url":"/get/config",
        "request_type": 'post',
        "execution_order": 1
    },



#################### ANALYTICS SERVER #####################

######## CREATE ANALYTIC EVENT LOG
    {
        "step_id":"",
        "service_id":"#11",
        "workflow_id":"$41",
        "relative_url":"/analytic/event-log",
        "request_type": 'post',
        "execution_order": 1
    },

######## DELETE ANALYTIC EVENT LOG
    {
        "step_id":"",
        "service_id":"#11",
        "workflow_id":"$42",
        "relative_url":"/analytic/event-log",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET ANALYTIC EVENT LOG
    {
        "step_id":"",
        "service_id":"#11",
        "workflow_id":"$43",
        "relative_url":"/get/analytic/event-log",
        "request_type": 'post',
        "execution_order": 1
    },

######## CREATE ANALYTIC METRIC
# get metric
    {
        "step_id":"",
        "service_id":"#11",
        "workflow_id":"$44",
        "relative_url":"/analytic/metric",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE ANALYTIC METRIC
    {
        "step_id":"",
        "service_id":"#11",
        "workflow_id":"$45",
        "relative_url":"/analytic/metric",
        "request_type": 'put',
        "execution_order": 1
    },

######## DELETE ANALYTIC METRIC
    {
        "step_id":"",
        "service_id":"#11",
        "workflow_id":"$46",
        "relative_url":"/analytic/metric",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET ANALYTIC METRIC
    {
        "step_id":"",
        "service_id":"#11",
        "workflow_id":"$47",
        "relative_url":"/get/analytic/metric",
        "request_type": 'post',
        "execution_order": 1
    },



#################### AUTH SERVER #####################

######## CREATE CREDENTIAL
# get credential
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$81",
        "relative_url":"/auth/credential",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE CREDENTIAL
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$82",
        "relative_url":"/auth/credential",
        "request_type": 'put',
        "execution_order": 1
    },


######## DELETE CREDENTIAL
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$83",
        "relative_url":"/auth/credential",
        "request_type": 'delete',
        "execution_order": 1
    },


######## GET CREDENTIAL
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$84",
        "relative_url":"/get/auth/credential",
        "request_type": 'post',
        "execution_order": 1
    },


######## CREATE SESSION
# get session
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$85",
        "relative_url":"/auth/session",
        "request_type": 'post',
        "execution_order": 2
    },


######## GET SESSION
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$86",
        "relative_url":"/get/auth/session",
        "request_type": 'post',
        "execution_order": 1
    },


######## DELETE SESSION
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$87",
        "relative_url":"/auth/credential",
        "request_type": 'delete',
        "execution_order": 1
    },


######## CREATE RESET-TOKEN
# get reset-token
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$88",
        "relative_url":"/auth/reset-token",
        "request_type": 'post',
        "execution_order": 2
    },

######## DELETE RESET-TOKEN
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$89",
        "relative_url":"/auth/reset-token",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET RESET-TOKEN
    {
        "step_id":"",
        "service_id":"#3",
        "workflow_id":"$90",
        "relative_url":"/get/auth/reset-token",
        "request_type": 'post',
        "execution_order": 1
    },



#################### BOOKING SERVER #####################

######## CREATE GUEST
# get guest
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$101",
        "relative_url":"/guest",
        "request_type": 'post',
        "execution_order": 2
    },

######## GET GUEST
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$102",
        "relative_url":"/get/guest",
        "request_type": 'post',
        "execution_order": 1
    },

######## DELETE GUEST
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$103",
        "relative_url":"/guest",
        "request_type": 'delete',
        "execution_order": 1
    },

######## CREATE BOOKING
# create guest
# get booking
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$104",
        "relative_url":"/booking",
        "request_type": 'post',
        "execution_order": 3
    },

######## GET BOOKING
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$105",
        "relative_url":"/get/booking",
        "request_type": 'post',
        "execution_order": 1
    },

######## DELETE BOOKING
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$106",
        "relative_url":"/booking",
        "request_type": 'delete',
        "execution_order": 1
    },

######## CREATE INVOICE
# get invoice
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$107",
        "relative_url":"/invoice",
        "request_type": 'post',
        "execution_order": 2
    },

######## GET INVOICE
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$108",
        "relative_url":"/get/invoice",
        "request_type": 'post',
        "execution_order": 1
    },

######## DELETE INVOICE
    {
        "step_id":"",
        "service_id":"#9",
        "workflow_id":"$109",
        "relative_url":"/invoice",
        "request_type": 'delete',
        "execution_order": 1
    },



#################### ROOM SERVER #####################

######## CREATE ROOM
# get room
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$121",
        "relative_url":"/room",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE ROOM
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$122",
        "relative_url":"/room",
        "request_type": 'put',
        "execution_order": 1
    },

######## DELETE ROOM
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$123",
        "relative_url":"/room",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET ROOM
# get amenity
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$124",
        "relative_url":"/get/room",
        "request_type": 'post',
        "execution_order": 2
    },

######## CREATE AMENITY
# get amenity
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$125",
        "relative_url":"/amenity",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE AMENITY
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$126",
        "relative_url":"/amenity",
        "request_type": 'put',
        "execution_order": 1
    },

######## DELETE AMENITY
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$127",
        "relative_url":"/amenity",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET AMENITY
# get amenity picture
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$128",
        "relative_url":"/get/amenity",
        "request_type": 'post',
        "execution_order": 2
    },

######## CREATE AMENITY PICTURE
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$129",
        "relative_url":"/amenity/picture",
        "request_type": 'post',
        "execution_order": 1
    },

######## UPDATE AMENITY PICTURE
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$130",
        "relative_url":"/amenity/picture",
        "request_type": 'put',
        "execution_order": 1
    },

######## DELETE AMENITY PICTURE
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$131",
        "relative_url":"/amenity/picture",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET AMENITY PICTURE
    {
        "step_id":"",
        "service_id":"#7",
        "workflow_id":"$132",
        "relative_url":"/get/amenity/picture",
        "request_type": 'post',
        "execution_order": 1
    },


#################### PAYMENT GATEWAY SERVER #####################

######## CREATE TRANSACTION
# get transaction
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$141",
        "relative_url":"/transaction",
        "request_type": 'post',
        "execution_order": 2
    },

######## DELETE TRANSACTION
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$142",
        "relative_url":"/transaction",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET TRANSACTION
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$143",
        "relative_url":"/get/transaction",
        "request_type": 'post',
        "execution_order": 1
    },

######## CREATE BANK
# get bank
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$144",
        "relative_url":"/bank",
        "request_type": 'post',
        "execution_order": 1
    },

######## UPDATE BANK
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$145",
        "relative_url":"/bank",
        "request_type": 'put',
        "execution_order": 1
    },

######## DELETE BANK
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$146",
        "relative_url":"/bank",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET BANK
    {
        "step_id":"",
        "service_id":"#8",
        "workflow_id":"$147",
        "relative_url":"/get/bank",
        "request_type": 'post',
        "execution_order": 1
    },


#################### REVIEW SERVER #####################

######## CREATE REVIEW
# get review
    {
        "step_id":"",
        "service_id":"#2",
        "workflow_id":"$161",
        "relative_url":"/review",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE REVIEW
    {
        "step_id":"",
        "service_id":"#2",
        "workflow_id":"$162",
        "relative_url":"/review",
        "request_type": 'put',
        "execution_order": 1
    },

######## DELETE REVIEW
    {
        "step_id":"",
        "service_id":"#2",
        "workflow_id":"$163",
        "relative_url":"/review",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET REVIEW
    {
        "step_id":"",
        "service_id":"#2",
        "workflow_id":"$164",
        "relative_url":"/get/review",
        "request_type": 'post',
        "execution_order": 1
    },



#################### TENANT SERVER #####################

######## CREATE TENANT
# get tenant
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$181",
        "relative_url":"/tenant",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE TENANT
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$182",
        "relative_url":"/tenant",
        "request_type": 'put',
        "execution_order": 1
    },

######## DELETE TENANT
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$183",
        "relative_url":"/tenant",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET TENANT
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$184",
        "relative_url":"/get/tenant",
        "request_type": 'post',
        "execution_order": 1
    },

######## CREATE BILLING
# get billing
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$185",
        "relative_url":"/billing",
        "request_type": 'post',
        "execution_order": 2
    },

######## DELETE BILLING
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$186",
        "relative_url":"/billing",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET BILLING
    {
        "step_id":"",
        "service_id":"#5",
        "workflow_id":"$187",
        "relative_url":"/get/billing",
        "request_type": 'post',
        "execution_order": 1
    },


#################### USER SERVER #####################

######## CREATE USER
# get user
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$201",
        "relative_url":"/user",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE USER
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$202",
        "relative_url":"/user",
        "request_type": 'put',
        "execution_order": 1
    },

######## DELETE USER
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$203",
        "relative_url":"/user",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET USER
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$204",
        "relative_url":"/get/user",
        "request_type": 'post',
        "execution_order": 1
    },

######## CREATE USER PROFILE
# get user profile
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$205",
        "relative_url":"/user/profile",
        "request_type": 'post',
        "execution_order": 2
    },

######## UPDATE USER PROFILE
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$206",
        "relative_url":"/user/profile",
        "request_type": 'put',
        "execution_order": 1
    },

######## DELETE USER PROFILE
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$207",
        "relative_url":"/user/profile",
        "request_type": 'delete',
        "execution_order": 1
    },

######## GET USER PROFILE
    {
        "step_id":"",
        "service_id":"#10",
        "workflow_id":"$208",
        "relative_url":"/get/user/profile",
        "request_type": 'post',
        "execution_order": 1
    },




]