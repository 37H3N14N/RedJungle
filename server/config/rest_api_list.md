-------------------------------------------
        REST APIs
-------------------------------------------

    [ Nginx ]

-> /hierarchy
-> /identity
-> /auth
-> /content


    [ Hierarchy ]

{POST} = ['post with necessary payload']
-> [/group/create], [/group/update], [/group/delete] 
-> [/folder/create], [/folder/update], [/folder/delete] 
-> [/note/create], [/note/update], [/note/delete] 

{GET} = ['uri with neccessary input']
-> [/group/read] 
-> [/folder/read] 
-> [/note/read] 


    [ Identity ]

{POST} = ['post with necessary payload']
-> [/user/create], [/user/update], [/user/delete] 
-> [/session/create], [/session/delete] 

{GET} = ['uri with neccessary input']
-> [/user/read] 
-> [/session/read] 


    [ Auth ]

{POST} = ['post with necessary payload']
-> [/group/create], [/group/update], [/group/delete] 
-> [/folder/create], [/folder/update], [/folder/delete] 
-> [/note/create], [/note/update], [/note/delete] 

{GET} = ['uri with neccessary input']
-> [/group/read] 
-> [/folder/read] 
-> [/note/read] 


    [ Content ]

{POST} = ['post with necessary payload']
-> [/content/create]
-> [/content/update]
-> [/content/delete] 

{GET} = ['uri with neccessary input']
-> [/content/read] 
























































