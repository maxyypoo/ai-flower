import sqlite3
from sqlite3 import Error
import atexit
import requests
import os
import json
from flask import Flask, render_template, requests, jsonify





con = sql_con()

@app.route('/')
def root():
  return render_template('index.html')

@app.route('/button_click', methods = ['POST'])
def clicked():
  #some information from front end, like qr_code id = ?, location_id = ?, js_token_string = ?, flower_id = ? in the form of list of dictionaries: ([key, pair], [key, pair] ...)
  frontEndInfo = requests.json['infos']
  #or information is passed individually as single strings: "location_id"
  frontEndInfo1 = requests.json['info']
  frontEndInfo2 = requests.json['info']
  #and so on...
  #we make a SELECT call to our db, using the sql class I wrote, or we make custom SELECT calls here to figure out the growth level of the flower or if the flower even exists for the given location yet
  myCursor = con.cursor()
  myCursor.execute('SELECT information FROM one_of_our_tables WHERE some_identifying_info = frontEndInfo')
  receivedInfo = myCursor.fetchall
  
@app.route('/display', methods = ['POST'])
def displayFlower():
  #here we calculate the flower that will be displayed based on previously acquired info, and send the specifications to front end
  

@atexit.register
def shutdown():
    if client:
        client.disconnect()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=True)
