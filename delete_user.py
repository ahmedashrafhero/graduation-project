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

db = DB.connect("localhost","root","","hm_security")
cursor = db.cursor(DB.cursors.DictCursor)
sql = 'DELETE FROM person WHERE name = "%s" AND typeID = %s' %(attr2 , attr1)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
cursor.close()
db.close()
