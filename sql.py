import sqlite3
from sqlite3 import Error


class sql:
  def sql_con():
    try:
      con = sqlite3.connect('mydb.db')
      return con
    except Error:
      print (Error)

  def insertIntoQr(con, entities):
    myCursor = con.cursor()
    myCursor.execute('INSERT INTO qr qr_code_bin VALUES ?' , entities)
    myCursor.commit()    
  
  def insertIntoFlower(con, entities):
    myCursor = con.cursor()
    myCursor.execute('INSERT INTO flower (growth_lvl, date_last_attended, _unique_clicks) VALUES (?, ?, ?)' , entities)
    myCursor.commit()
    
    
  def insertIntoQr(con, entities):
    myCursor = con.cursor()
    myCursor.execute('INSERT INTO js (js_token_string, is_active) VALUES (?, ?)' , entities)
    myCursor.commit()