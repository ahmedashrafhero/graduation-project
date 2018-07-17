#!C:/Python27/python.exe
# Import modules for CGI handling 
import cgi, cgitb
import MySQLdb as DB

print "Content-type: application/xml \r\n"
def parse_it(tup):
    rang = len(tup)
    content = '<?xml version="1.0" encoding="UTF-8"?> \r\n'
    content += "<tags>\r\n"
    for i in range(rang):
        content += "<tag"+str(i)+">\r\n"
        row = tup[i]
        for key in row.keys():
            content+= "<"+str(key)+">"+str(row[str(key)])+"</"+str(key)+">\r\n"
        content += "</tag"+str(i)+">\r\n"
    content += "</tags>\r\n"
    return content

# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
attr1  = form.getvalue('attr1')

db = DB.connect("localhost","root","","hm_security")
cursor = db.cursor(DB.cursors.DictCursor)
sql = '''SELECT person.name, data.content, data.image, notification.dateAndTime FROM person, notification, data, relative WHERE person.person = relative.relativeID AND notification.dataID = data.ID AND relative.relativeID = data.relativeID AND person.person = %s''' % attr1
cursor.execute(sql)
data = cursor.fetchall()
print parse_it(data)
cursor.close()
db.close()
