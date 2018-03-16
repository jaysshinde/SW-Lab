''' File for handling the main_database
    This file contains all functions that may be required for managing the
    database.

    Dependencies: sqlite3,pysqlcipher

'''
import sqlite3
import os
import random
from passlib.hash import pbkdf2_sha256 as hasher
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
        db_access = 1416
        return db_access

    except sqlite3.OperationalError:
        cur = db.cursor()
        cur.execute("DROP TABLE IF EXISTS ItemMaster")
        cur.execute("DROP TABLE IF EXISTS TaxRates")
        cur.execute("DROP TABLE IF EXISTS Transactions")
        cur.execute("DROP TABLE IF EXISTS Users")

        cur.execute("""CREATE TABLE `ItemMaster` (
	         `ItemID`	INTEGER NOT NULL PRIMARY KEY UNIQUE,
	         `ItemName`	TEXT NOT NULL,
	         `Category`	TEXT NOT NULL,
	         `Price`	REAL NOT NULL,
	         `Unit_s`	INTEGER NOT NULL,
	         `Quantity`	REAL NOT NULL,
	         `Remarks`	TEXT)"""
                             )
        cur.execute("""CREATE TABLE `TaxRates` (
	       `ItemID`	INTEGER NOT NULL UNIQUE,
	       `ProductTax`	REAL NOT NULL,
	       `GST`	REAL NOT NULL,
	       `AdditionalTaxes`	REAL,
	       `Remarks`	TEXT,
	       FOREIGN KEY(`ItemID`) REFERENCES `ItemMaster`(`ItemID`)
                          )""")
        cur.execute("""CREATE TABLE `Transactions` (
        	`TransID`	INTEGER NOT NULL,
        	`ItemID`	INTEGER NOT NULL,
        	`Sales_Purchase`	TEXT NOT NULL,
        	`Quantity`	REAL NOT NULL,
        	`Cost`	REAL NOT NULL,
        	`Tax`	REAL NOT NULL,
        	`UserID`	INTEGER NOT NULL,
            FOREIGN KEY(`ItemID`) REFERENCES `ItemMaster`(`ItemID`),
        	FOREIGN KEY(`UserID`) REFERENCES `Users`(`UserID`)
        )""")

        cur.execute("""CREATE TABLE `Users` (
        	`UserID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        	`Username`	TEXT NOT NULL UNIQUE,
        	`Password`	TEXT NOT NULL,
            'EmailID'  TEXT NOT NULL UNIQUE,
        	`Class`	TEXT NOT NULL,
        	`Comments`	TEXT
        )""")
        db.commit()
        db_access = 1416
        return db_access

#Function only for master user insecure right now
def access_user():
    with sqlite3.connect(db_name) as db:
        cur = db.cursor()
        cur.execute("SELECT * FROM Users")
        res = cur.fetchall()

    return res,len(res)

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
                    cur.execute("SELECT Class FROM Users WHERE Username = ?",(self.name,))
                    res = cur.fetchall()
                    self.uclass = res[0][0]
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


class Trans(User):
    def __init__(self,transid,count,info,name,cat):
        self.transid = transid
        self.count = count
        self.info = info
        self.name = name
        self.cat = cat
        # In list info
        # Index 0 is for Item ID
        # Index 1 is for Item Name
        # Index 2 is for quantity

        with sqlite3.connect(db_name) as db:
            cur = db.cursor()
            cur.execute("SELECT UserID FROM Users WHERE Username = ?",(self.name,))
            res = cur.fetchall()
            self.uid = res[0]

        self.cost = []
        self.taxes = []


    #Retreives calculated tax to be added to the Transcation table
    #Update Tax Column
    def retreive(self):
        with sqlite3.connect(db_name) as db:
            cur = db.cursor()
            for i in range(0,self.count):
                cur.execute("SELECT * FROM TaxRates WHERE ItemID = ?",(self.info[i][0],))
                res = cur.fetchall()
                self.rates = res
                val = float(0)
                for j in range(1,4):
                    if( self.rates[0][j] != None):
                        val = val + ((self.cost[i] * float(self.rates[0][j]))/100)
                self.taxes.append(val)


            # Fetched all data till now
            #Process and add remaining stuff
    def price_calc(self):
        # Calculate Prices from quantity update Cost Column'''
        with sqlite3.connect(db_name) as db:
            cur = db.cursor()
            for i in range(0,self.count):
                cur.execute("SELECT Price,Unit_s FROM ItemMaster WHERE  ItemID = ?",(self.info[i][0],))
                res = cur.fetchall()
                val = float(res[0][0]) * (float(self.info[i][2])/float(res[0][1]))
                print val
                self.cost.append(val)

    def to_database(self):
        self.tid = random.randint(1,100000)
        with sqlite3.connect(db_name) as db:
            cur = db.cursor()
            for i in range(0,self.count):
                cur.execute("INSERT INTO Transactions(TransID,ItemID,Sales_Purchase,Quantity,Cost,Tax,UserID) VALUES (?,?,?,?,?,?,?)",(self.tid,int(self.info[i][0]),self.cat,int(self.info[i][2]),self.cost[i],float(self.taxes[i]),int(self.uid[0]),))

    def inventory(self):
        with sqlite3.connect(db_name) as db:
            cur = db.cursor()
            for i in range(0,self.count):
                cur.execute("SELECT Quantity FROM ItemMaster WHERE ItemID = ?",(self.info[i][0],))
                res = cur.fetchall()
                res = int(res[0][0])
                demand = int(self.info[i][2])
                quan = res - demand

                if(quan < 0):
                    return 113
                elif(quan >= 0):
                    cur.execute("UPDATE ItemMaster SET Quantity = ? WHERE ItemID = ?",(quan,self.info[i][0],))




    def dothis(self):
        try:
            self.price_calc()
            self.retreive()
            self.to_database()
            val = self.inventory()
            if(val == 113):
                return -1
            else:
                return 1
        except:
            return 0
