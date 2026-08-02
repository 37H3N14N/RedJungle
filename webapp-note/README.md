---------------------------
    [   NOTE    ] 
---------------------------

> /group/

> /folder/

> /note/

Options
= /content
= /detail
= crud option for all endpoints 

---------------------------
    Role Features 
---------------------------

> Group Creator
- make group private/public
- make folder private/public
- apoint folder admin
- crud folders
- visibility of everything

> Folder Admin 
- visibility of notes in folder
- add/revoke members to/from folder 
- delete member notes

> Member
- make own notes private 
- revoke members from note
- visibility of private group
- visibility of private invited folder

> Anyone
- crud note 
- automatic backed notes on user private group 


> Public Groups/Folder
- read by anyone only for the public content within

> Private Groups/Folder
- read only by the curated members

> Private Notes
- read by curated folder members
- read by group owner and folder admin


----------------------
    Database 
----------------------

> Identity :
- user signup/login/update 
{ user_id, username, passcode }

- session_id 
{ user_id, session_id }

> Hierarchy Record :
- Group crud
{ creator_user_id, group_id,name }

- Folder crud
{ creator_member_id, folder_id,name }

- Note crud
{ creator_member_id, note_id,name }


> Note :

- note data 
{ data_id, user_id, note_id,data_content, timestamp}


> Member Relation:
- Group Members
{ member_id,group_id, user_id }

- Super Members
{ group_id, member_id,admin_resource/folder/chat, 
  resource_id }

- Folder Members
{ member_id,Folder_id}

- Note Members
{ member_id ,Note_id}


-----------------------------
    CURLS 
-----------------------------

NB: Mostly using Get request with special headers to allow for quasi post requests for simplicity but covers everything .... remember this is the rugged-jungle[RJ]

curl
-H 'userid: u_5'
-H 'item_id: ch_01'
-H 'action: read'
http://localhost:5000/chat/detail 
= one/all chats in the folder of user


curl
-H 'userid: u_5'
-H 'item_id: f_2'
-H 'action: read'
http://localhost:5000/folder/detail or contents
= all chats in the folder


curl
-H 'userid: u_5'
-H 'item_id: g_3'
-H 'action: read'
http://localhost:5000/group/detail or contents
= group details
= all folders in the group


curl
-H 'userid: u_5'
-H 'item_id: g_3'
-H 'action: read'
http://localhost:5000/home
= all groups


