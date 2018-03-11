''' File for handling the main_database
    This file contains all functions that may be required for managing the
    database.

    Dependencies: sqlite3,pysqlcipher

'''
import sqlite3
import os
#from pysqlcipher import dbapi2 as sqlcipher

db_name = "main_database.db"

######################################################
## Function for setting up the database or ensuring ##
## that database with correct strutcture exists     ##
######################################################
def setup_check():

    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute("PRAGMA foreign_keys=ON")
        db.commit()


    try:
        cur = db.cursor()
        cur.execute("SELECT COUNT(*) FROM ItemMaster")
        var = cur.fetchall()
        cur.execute("SELECT COUNT(*) FROM TaxRates")
        var = cur.fetchall()
        cur.execute("SELECT COUNT(*) FROM Transactions")
        var = cur.fetchall()
        cur.execute("SELECT COUNT(*) FROM Users")
        var = cur.fetchall()
        db.commit()

    except sqlite3.OperationalError:
        cur = db.cursor()
        cur.execute("DROP TABLE IF EXISTS ItemMaster")
        cur.execute("DROP TABLE IF EXISTS TaxRates")
        cur.execute("DROP TABLE IF EXISTS Transactions")
        cur.execute("DROP TABLE IF EXISTS Users")

        cur.execute("""CREATE TABLE `ItemMaster` (
	         `Item ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	         `Item Name`	TEXT NOT NULL,
	         `Category`	TEXT NOT NULL,
	         `Price`	REAL NOT NULL,
	         `Unit_s`	INTEGER NOT NULL,
	         `Quantity`	REAL NOT NULL,
	         `Remarks`	TEXT)"""
                             )
        cur.execute("""CREATE TABLE `TaxRates` (
	       `Item ID`	INTEGER NOT NULL,
	       `Product Tax`	REAL NOT NULL,
	       `GST`	REAL NOT NULL,
	       `Additional Taxes`	REAL,
	       `Remarks`	TEXT,
	       FOREIGN KEY(`Item ID`) REFERENCES `ItemMaster`(`Item ID`)
                          )""")
        cur.execute("""CREATE TABLE `Transactions` (
        	`Trans ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        	`Item ID`	INTEGER NOT NULL,
        	`Sales/Purchase`	TEXT NOT NULL,
        	`Quantity`	REAL NOT NULL,
        	`Cost`	REAL NOT NULL,
        	`Tax`	REAL NOT NULL,
        	`User ID`	INTEGER NOT NULL,
        	FOREIGN KEY(`User ID`) REFERENCES `Users`(`User ID`)
        )""")

        cur.execute("""CREATE TABLE `Users` (
        	`User ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        	`Username`	TEXT NOT NULL UNIQUE,
        	`Password`	TEXT NOT NULL,
            'EmailID'  TEXT NOT NULL UNIQUE,
        	`Class`	TEXT NOT NULL,
        	`Comments`	TEXT
        )""")
        db.commit()
        db_access = 1416
        return db_access

######################################################
##                                                  ##
##  Classes for accessing data from the database    ##
######################################################
class User(object):
    def __init__(self,name="", pwd="", email="", uclass="",flag=0):
        self.name = name
        self.pwd = pwd
        self.email = email
        self.uclass = uclass
        self.flag = flag

    def check(self):
        with sqlite3.connect(db_name) as db:
            cur = db.cursor()
            cur.execute("SELECT * FROM Users WHERE Username = ?",(self.name,))
            res = cur.fetchall()
            if(len(res) == 0):
                return 0
            else:
                if(res[0][2] == self.pwd):
                    return 1
    def sign_proc(self):
        ret = self.check()
        if(ret == 0):
            with sqlite3.connect(db_name) as db:
                cur = db.cursor()
                try:
                    cur.execute("INSERT INTO Users(Username, Password, EmailID, Class) VALUES (?,?,?,?)",(self.name,self.pwd,self.email,self.uclass,))
                    db.commit()
                    return 0
                except sqlite3.OperationalError:
                    return -2 #-2 is for Email ID being not UNIQUE
        else:
            return -1 #-1 is for Username being not unique
