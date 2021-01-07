import streamlit as st
import numpy as np
import pandas as pd 
#import matplotlib.pyplot as plt
#import seaborn as sns
import pymysql
st.title("hello - there!")
import mysql.connector
mydb = mysql.connector.connect(
    host="mysql-development",
    user="root",
    password="jb",
    database = "suicide-app"
)
print(mydb)
cursor = mydb.cursor()
sql = "CREATE TABLE regions (id INT AUTO_INCREMENT PRIMARY KEY, region VARCHAR(255));"
cursor.execute(sql)

