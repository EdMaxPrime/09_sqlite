import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f = "discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE
peepsFile = open("peeps.csv", "r")
students = csv.DictReader(peepsFile)
for row in students:
    print row

command = ""          #put SQL statement in this string
c.execute(command)    #run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database
peepsFile.close() #close file


