#!/usr/bin/env python



'''
--------------------------------------------------
--------------------------------------------------
 @ Module: Database Connector 
 @ Name:   GeeksForGeeks Article Extractor
 @ Purpose: To download and save articles filed under each and every tag mentioned in www.geeksforgeeks.org 
 @ Author: Debapriya Das
 	Dept of CSE, NIT Durgapur

V1.0 - 06.04.2015 - dbupdate search and keep records for later data analytics

 # MIT License - used for non-commercial purposes, used for college project work
 # Special thanks to - GeeksForGeeks.org

--------------------------------------------------
--------------------------------------------------
'''


import MySQLdb


# saves the search histories into the database for data analysis in future

def dbSave(name, email, search) :
	db = MySQLdb.connect(   host="localhost", # your host, usually localhost
				port =3306, # port on which MySQL is running
                     		user="root", # your username
                      		passwd="admin", # your password
                      		db="geeksforgeeks") # name of the database
        cur=db.cursor()
	#SQL query to INSERT a record into the table RECORDS.
	cur.execute("INSERT INTO Records (name, email, search_string) VALUES(%s, %s, %s)", (name, email, search))

	db.commit()




