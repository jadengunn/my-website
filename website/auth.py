from flask import Blueprint, render_template, request, flash
import pyodbc as odbc
from bs4 import BeautifulSoup

auth = Blueprint('auth', __name__)

server = 'cpsc.database.windows.net'
database = 'CPSC'
username = 'CPSC'
password = 'Meepbit1'
driver= '{ODBC Driver 18 for SQL Server}'

#Creating connection
#conn = odbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)


#Creating new cursor object from connection
#cursor = conn.cursor()

#Select Query
#select_sql = "SELECT * FROM [Manager]"

#Execute Select Query
#cursor.execute(select_sql)

#Insert Query
#insert_sql = "INSERT INTO [Manager] (FirstName, LastName, Email) VALUES (?, ?, ?)"

#records = [
    #(FirstName, LastName, Email)
#]

#cursor.executemany(insert_sql, records)
#cursor.commit()
#dataset = cursor.fetchall()
#print(dataset)

#Closing conection
#conn.close()

@auth.route('/login', methods=['GET', 'POST'])
def login( ):
    #Check if records match with database
    #If yes --> send to home.html
    #If no --> Message Flash("Incorrect password")
    return render_template("login.html")


@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        conn = odbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        FirstName = request.form.get("FirstName")
        LastName = request.form.get("LastName")
        Email = request.form.get("email")
        cursor = conn.cursor()
        insert_sql = "INSERT INTO [Manager] (FirstName, LastName, Email) VALUES (?, ?, ?)"
        records = [
    (FirstName, LastName, Email)
    ]
        cursor.executemany(insert_sql, records)
        cursor.commit()
        #dataset = cursor.fetchall()
        #print(dataset)
        conn.close()
        #return ("First Name: " + FirstName + " Last Name: " + LastName + " Email: " + Email)
    return render_template("sign_up.html")



@auth.route('/recall')
def recall():
    return render_template("recall.html")

@auth.route('/search')
def search():
    return render_template("search.html")