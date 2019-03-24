#!/usr/bin/python3
# make sure that the db proxy is running in its own terminal

import pymysql
import os

class Database:
    def __init__(self):
        self._db_un = os.environ['DB_UN']
        self._db_pw = os.environ['DB_PW']

        # Open database connection
        self._con = pymysql.connect(host='127.0.0.1', user=self._db_un, password=self._db_pw, db='trashtag')

    def __del__(self):
        self.disconnect();
    
    def connect(self):
        self._con = pymysql.connect(host='127.0.0.1', user=self._db_un, password=self._db_pw, db='trashtag')

    def disconnect(self):
        if self._con:
            self._con.commit();
            self._con.close();

    def getItems(self):
        cursor = self._con.cursor()
        # execute SQL query using execute() method.
        cursor.execute("SELECT * FROM item")

        # retrieve cursor results
        res = cursor.fetchall()

        return res
    
    def insertItem(self, type):
        mycursor = self._con.cursor()

        sql = "INSERT INTO item (type) VALUES (%s)"
        mycursor.execute(sql, type)

        self._con.commit()

