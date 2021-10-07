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
    myCursor.execute('INSERT INTO flower (growth_lvl, date_last_attended, unique_clicks) VALUES (?, ?, ?)' , entities)
    myCursor.commit()
    
    
  def insertIntoQr(con, entities):
    myCursor = con.cursor()
    myCursor.execute('INSERT INTO js (js_token_string, is_active) VALUES (?, ?)' , entities)
    myCursor.commit()
    
  def updateFlower(con, entities):
    myCursor = con.cursor()
    myCursor.execute('UPDATE flower SET growth_lvl = growth_lvl + 1, date_last_attended = ?, unique_clicks = ? WHERE flower_id = (SELECT flower_id from js WHERE js_token_string = ?)' , entities)
    myCursor.commit()
    
    
  def updateJs(con, entities):
    myCursor = con.cursor()
    myCursor.execute('UPDATE js SET is_active = ? WHERE js_token_string = ?' , entities)
    myCursor.commit()
    
  def updateLoc(con, entities):
    myCursor = con.cursor()
    myCursor.execute('UPDATE location SET total_visits = ?, total_unique_visits = ? WHERE location_id = ?' , entities)
    myCursor.commit()