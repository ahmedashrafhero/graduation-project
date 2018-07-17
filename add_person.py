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
attr5  = form.getvalue('attr5')
attr6  = form.getvalue('attr6')
attr7  = form.getvalue('attr7')

db = DB.connect("localhost","root","","hm_security")
cursor = db.cursor()
sql = 'SELECT MAX(IF(owner.Email = "%s",1,0)) FROM owner' % attr5
cursor.execute(sql)
dig = cursor.fetchall()
cursor.close()

if int(dig[0][0]) == 0:
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
    sql = 'INSERT INTO owner VALUES(%s , "%s" , "%s" , %s , %s) ;' % (int(ID[0][0]),attr4,attr5,attr6,attr7)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    cursor.close()
else :
    print "ERROR IN YOUR REQUEST"
db.close()
