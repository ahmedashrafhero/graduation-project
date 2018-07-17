get owner data by username and password
http://localhost/python/get_owner_data.py?attr1=USERNAME&attr2=PASSWORD
where USERNAME => the username (String) and PASSWORD => the password (String)
example : username = ahmed , password = 12345

get visitor data by the person ID
http://localhost/python/get_visitor_data.py?attr1=ID
example : ID (int) = 2

add person to db
http://localhost/python/add_person.py?attr1=ayman&attr2=fig.jpg&attr3=1&attr4=123456&attr5=ayman@fci.com&attr6=2&attr7=0
USERNAME = ayman (String)
NAME of IMAGE = **.jpg or **.png (String)
attr3 => typeID (int) 
attr4 => password (String)
attr5 => email (String)
attr6 => adminoruser (int)
attr7 => communicationflag (int)

add relative to each person and relative_table
http://localhost/python/add_relat.py?attr1=ali&attr2=fig.png&attr3=2&attr4=ali'sfather
attr1 => username of relative (String)
attr2 => name of his/her image (string)
attr3 => typeID (int)
attr4 => relation of this person to anyone (String)

delete user(owner) from table owner and person
http://localhost/python/delete_user.py?attr1=2&attr2=adham
attr1 = typeID (int)
attr2 = name (String)

delete relative from person and relative
http://localhost/python/delete_relat.py?attr2=ali&attr1=2
attr2 => name (String)
attr1 => typeID (int)

get owner data by his/her name for searching
http://localhost/python/owner_data.py?attr1=ahmed
attr1 => his/her name or part of his/her owner name (String)

get relative data also by his/her name
http://localhost/python/realt_data.py?attr1=fa
attr1 => his/her name or part of his/her relative name (String)



