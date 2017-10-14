import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f = "discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
peepsFile = open("peeps.csv", "r")
students = csv.DictReader(peepsFile)

command = "CREATE TABLE peeps (id INTEGER PRIMARY KEY, name STRING, age INTEGER);"
c.execute(command)    #run SQL statement
for row in students:
    values = '(' + row['id'] + ', "' + row['name'] + '", ' + row['age'] + ');'
    c.execute("INSERT INTO peeps VALUES " + values)

#==========================================================
db.commit() #save changes
db.close()  #close database
peepsFile.close() #close file


