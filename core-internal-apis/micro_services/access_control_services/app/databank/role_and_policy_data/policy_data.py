policy_data = [

####################### ACCESS CONTROL SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#4",
        "roles":['#e'],
        "uri":"/role",
        "actions":['post','put','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#4",
        "roles":['#a'],
        "uri":"/get/role",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#4",
        "roles":['#e']
        "uri":"/policy",
        "actions":['post','put','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#4",
        "roles":['#a']
        "uri":"/get/policy",
        "actions":['post']
    },

####################### HOTEL SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#a']
        "uri":"/get/hotel",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#c']
        "uri":"/hotel",
        "actions":['put']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#e']
        "uri":"/hotel",
        "actions":['post','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#a']
        "uri":"/get/hotel-service",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#c']
        "uri":"/hotel-service",
        "actions":['put']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#e']
        "uri":"/hotel-service",
        "actions":['post','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#e','#d']
        "uri":"/booking-service",
        "actions":['post','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#e','#d','#c']
        "uri":"/booking-service",
        "actions":['get']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#c','#e']
        "uri":"/get/config",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#6",
        "roles":['#e']
        "uri":"/config",
        "actions":['post','put','delete']
    },

####################### ANALYTIC SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#11",
        "roles":['#c','#e']
        "uri":"/analytic/event-log",
        "actions":['delete']
    },

    {
        "policy_id":"$",
        "service_id":"#11",
        "roles":['#c','#e']
        "uri":"/get/analytic/event-log",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#11",
        "roles":['#a']
        "uri":"/analytic/event-log",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#11",
        "roles":["#c",'#e']
        "uri":"/analytic/metric",
        "actions":['put','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#11",
        "roles":["#c",'#e']
        "uri":"/get/analytic/metric",
        "actions":['post']
    },

####################### AUDIT LOGGING SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#12",
        "roles":['#a']
        "uri":"/audit",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#12",
        "roles":['#c','#e']
        "uri":"/audit",
        "actions":['delete']
    },

    {
        "policy_id":"$",
        "service_id":"#12",
        "roles":['#c','#e']
        "uri":"/get/audit",
        "actions":['post']
    },

####################### AUTH SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#3",
        "roles":['#a']
        "uri":"/auth/credential",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#3",
        "roles":['#b']
        "uri":"/auth/credential",
        "actions":['put']
    },

    {
        "policy_id":"$",
        "service_id":"#3",
        "roles":['#b','#e']
        "uri":"/auth/credential",
        "actions":['delete']
    },

    {
        "policy_id":"$",
        "service_id":"#3",
        "roles":['#b','#e']
        "uri":"/get/auth/credential",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#3",
        "roles":['#a']
        "uri":"/get/auth/session",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#3",
        "roles":['#b','#e']
        "uri":"/auth/session",
        "actions":['delete']
    },

    {
        "policy_id":"$",
        "service_id":"#3",
        "roles":['#b','#e']
        "uri":"/get/auth/reset-token",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#3",
        "roles":['#b']
        "uri":"/auth/reset-token",
        "actions":['delete']
    },

####################### BOOKING SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#9",
        "roles":['#b','#c','#e']
        "uri":"/get/guest",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#9",
        "roles":['#b']
        "uri":"/guest",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#9",
        "roles":['#d','#c']
        "uri":"/guest",
        "actions":['delete']
    },

    {
        "policy_id":"$",
        "service_id":"#9",
        "roles":['#d']
        "uri":"/booking",
        "actions":['post','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#9",
        "roles":['#d','#c','#e']
        "uri":"/get/booking",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#9",
        "roles":['#d']
        "uri":"/invoice",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#9",
        "roles":['#d','#c','#e']
        "uri":"/invoice",
        "actions":['delete']
    },

    {
        "policy_id":"$",
        "service_id":"#9",
        "roles":['#d','#c','#e']
        "uri":"/get/invoice",
        "actions":['post']
    },

####################### ROOM SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#e','#a','#c']
        "uri":"/get/room",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#e','#c']
        "uri":"/room",
        "actions":['delete']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#c']
        "uri":"/room",
        "actions":['post','put']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#e','#a','#c']
        "uri":"/get/amenity",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#e','#c']
        "uri":"/amenity",
        "actions":['delete']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#c']
        "uri":"/amenity",
        "actions":['post','put']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#a']
        "uri":"/get/amenity/picture",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#c']
        "uri":"/amenity/picture",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#7",
        "roles":['#c','#e']
        "uri":"/amenity/picture",
        "actions":['delete']
    },

####################### ORCHESTRATION SERVER ##########################

####################### PAYMENT GATEWAY SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#8",
        "roles":['#b','#e']
        "uri":"/get/transaction",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#8",
        "roles":['#b']
        "uri":"/transaction",
        "actions":['post','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#8",
        "roles":['#b','#e']
        "uri":"/bank",
        "actions":['delete']
    },

    {
        "policy_id":"$",
        "service_id":"#8",
        "roles":['#b','#e']
        "uri":"/get/bank",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#8",
        "roles":['#e']
        "uri":"/bank",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#8",
        "roles":['#b']
        "uri":"/bank",
        "actions":['put']
    },

####################### REVIEW SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#2",
        "roles":['#a']
        "uri":"/get/review",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#2",
        "roles":['#d']
        "uri":"/review",
        "actions":['post','put']
    },

    {
        "policy_id":"$",
        "service_id":"#2",
        "roles":['#c','#d','#e']
        "uri":"/review",
        "actions":['delete']
    },

####################### TENANT SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#5",
        "roles":['#e','#f']
        "uri":"/tenant",
        "actions":['delete']
    },

    {
        "policy_id":"$",
        "service_id":"#5",
        "roles":['#e','#f']
        "uri":"/get/tenant",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#5",
        "roles":['#e']
        "uri":"/tenant",
        "actions":['post','put']
    },

    {
        "policy_id":"$",
        "service_id":"#5",
        "roles":['#e','#f']
        "uri":"/billing",
        "actions":['delete']
    },

    {
        "policy_id":"$",
        "service_id":"#5",
        "roles":['#e','#f']
        "uri":"/get/billing",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#5",
        "roles":['#e']
        "uri":"/billing",
        "actions":['post']
    },

####################### USER SERVER ##########################
    {
        "policy_id":"$",
        "service_id":"#10",
        "roles":['#b','#e','#f']
        "uri":"/get/user",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#10",
        "roles":['#b']
        "uri":"/user",
        "actions":['post','put','delete']
    },

    {
        "policy_id":"$",
        "service_id":"#10",
        "roles":['#b','#e','#f']
        "uri":"/get/user/profile",
        "actions":['post']
    },

    {
        "policy_id":"$",
        "service_id":"#10",
        "roles":['#b']
        "uri":"/user/profile",
        "actions":['post','put','delete']
    }






]