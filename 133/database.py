import sqlite3 as lite
import pandas as pd

con = lite.connect('database.db')

with con:
  cur = con.cursor()
  
  #creating table
  cur.execute('DROP TABLE IF EXISTS cities')
  cur.execute('DROP TABLE IF EXISTS weather')
  cur.execute('CREATE TABLE cities (name text, state text);')    
  cur.execute('CREATE TABLE weather (city text, year integer, warm_month text, cold_month text, average_high integer);')    
  
  #inserting data
  cur.execute("INSERT INTO cities VALUES('Washington', 'DC')")
  cur.execute("INSERT INTO cities VALUES('Houston', 'TX')")
  cur.execute("INSERT INTO cities VALUES('San Francisco', 'CA')")
  cur.execute("INSERT INTO cities VALUES('Los Angeles', 'CA')")

  cur.execute("INSERT INTO weather VALUES('Washington', 2013, 'July', 'January','60')")
  cur.execute("INSERT INTO weather VALUES('Houston', 2013, 'July', 'January', '61')")
  cur.execute("INSERT INTO weather VALUES('San Francisco', 2013, 'September', 'December', '64')")
  cur.execute("INSERT INTO weather VALUES('Los Angeles', 2013, 'September', 'December', '75')")

  #Joining table 
  cur.execute("SELECT name, state, year, warm_month, cold_month FROM cities INNER JOIN weather ON name = city;")
  data = cur.fetchall()
  cols = [desc[0] for desc in cur.description]
  df = pd.DataFrame(data, columns = cols)
  print(df)

  #displaying the data 
  cur.execute("SELECT city FROM weather ORDER BY average_high DESC;")
  outputName = cur.fetchall()
  
  # printing result
  print("The hottest to the coldest cities are: ")
  print(outputName)
  # ************* formating issue to be discussed in the next session
  # ************* http://stackoverflow.com/questions/11264684/flatten-list-of-lists
  # why the output is two dimension array while it seems there is no flatten functio in python
  # best way to display result
  print(outputName[0][0])

  cur.execute('SELECT SQLITE_VERSION()')
  # You're fetching the data from the cursor object. Because you're only fetching one record, you'll use the `fetchone()` method. If fetching more than one record, use the `fetchall()` method.
  data = cur.fetchone()
  # Finally, print the result.
  print("SQLite version: %s" % data)