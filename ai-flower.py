import sqlite3
from sqlite3 import Error
import atexit
import requests
import os
import json
from flask import Flask, render_template, requests, jsonify

def sql_con():
  try:
    con = sqlite3.connect('mydb.db')
    return con
  except Error:
    print (Error)
    
con = sql_con()
