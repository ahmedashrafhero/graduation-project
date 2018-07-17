#!C:/Python27/python.exe
# Import modules for CGI handling 
import cgi, cgitb
import MySQLdb as DB

print "Content-type: text/html\r\n"

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
attr1  = form.getvalue('attr1')
attr2  = form.getvalue('attr2')
attr3  = form.getvalue('attr3')
attr4  = form.getvalue('attr4')

db = DB.connect("localhost","root","","hm_security")


cursor = db.cursor()
sql = 'INSERT INTO person VALUES(NULL , "%s" , "%s" , %s) ;' % (attr1,attr2,attr3)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
cursor.close()

cursor = db.cursor()
sql = 'SELECT MAX(person.person) FROM person ;'
cursor.execute(sql)
ID = cursor.fetchall()
cursor.close()

cursor = db.cursor()
sql = 'INSERT INTO relative VALUES(%s , "%s") ;' % (int(ID[0][0]),attr4)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
cursor.close()

db.close()
