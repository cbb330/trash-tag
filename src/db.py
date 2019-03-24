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
        self.disconnect()
    
    def connect(self):
        self._con = pymysql.connect(host='127.0.0.1', user=self._db_un, password=self._db_pw, db='trashtag')

    def disconnect(self):
        if self._con:
            self._con.commit()
            self._con.close()

    def getItems(self):
        cursor = self._con.cursor()
        # execute SQL query using execute() method.
        cursor.execute("SELECT * FROM item")

        # retrieve cursor results
        res = cursor.fetchall()

        cursor.close()

        return res
    
    def getPerson(self, f_name, l_name):
        cursor = self._con.cursor()
        name = (f_name, l_name)

        sql = "SELECT * FROM person WHERE f_name=%s and l_name=%s"

        cursor.execute(sql, name)
        
        res = cursor.fetchall()

        cursor.close()
        return res
    
    def insertItem(self, type):
        cursor = self._con.cursor()

        sql = "INSERT INTO item (type) VALUES (%s)"
        cursor.execute(sql, type)

        cursor.close()
        self._con.commit()

    def insertPerson(self, organization, f_name, l_name, img, points=0):
        cursor = self._con.cursor()
        args = (organization, f_name, l_name, img, points)
        
        sql = "INSERT INTO person (organization, f_name, l_name, img, points) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, args)

        cursor.close()
        self._con.commit()

    def insertFaceAndHolding(self, confidence, date, img, oid, pid):
        cursor = self._con.cursor()
        args = (confidence, date, img, oid, pid)

        sql = "INSERT INTO face_and_holding (confidence, date, img, oid, pid) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, args)

        cursor.close()
        self._con.commit()
    
    def addPersonPoint(self, pid):
        cursor = self._con.cursor()

        sql = "UPDATE person SET points = points + 1 WHERE pid=%s"
        
        cursor.execute(sql, pid)

        cursor.close()
        self._con.commit()