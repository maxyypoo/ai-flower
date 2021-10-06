import sqlite3
from sqlite3 import Error
def sql_con():
  try:
    con = sqlite3.connect('mydb.db')
    return con
  except Error:
    print (Error)
    
def sql_table(con) :
  myCursor = con.cursor()
  myCursor.execute("CREATE TABLE IF NOT EXISTS qr (qr_id integer PRIMARY KEY AUTOINCREMENT, qr_code_bin varbinary(255) NOT NULL, flower_id integer NOT NULL, location_id integer NOT NULL)")
  con.commit()
  myCursor.execute("CREATE TABLE IF NOT EXISTS flower (flower_id integer PRIMARY KEY AUTOINCREMENT, growth_lvl integer NOT NULL, unique_clicks integer NOT NULL, date_last_attended date, location_id integer NOT NULL )")
  con.commit()
  myCursor.execute("CREATE TABLE IF NOT EXISTS js (token_id integer PRIMARY KEY AUTOINCREMENT, js_token_string varchar(32) NOT NULL, is_active bool NOT NULL, qr_id integer NOT NULL, location_id integer NOT NULL)")
  con.commit()
  myCursor.execute("CREATE TABLE IF NOT EXISTS location (location_id integer PRIMARY KEY AUTOINCREMENT, qr_id integer NOT NULL, location_name varchar(10) NOT NULL, total_visits integer, total_unique_visits integer)")
  con.commit()

con = sql_con()
sql_table(con)