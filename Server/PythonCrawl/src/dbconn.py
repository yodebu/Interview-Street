#!/usr/bin/env python



'''
--------------------------------------------------
--------------------------------------------------
 @ Name:   GeeksForGeeks Article Extractor
 @ Purpose: To download and save articles filed under each and every tag mentioned in www.geeksforgeeks.org 
 @ Author: Debapriya Das
 	Dept of CSE, NIT Durgapur

V1.0 - 06.04.2015 - dbupdate search and keep records

 # MIT License - used for non-commercial purposes, used for college project work
 # Special thanks to - GeeksForGeeks.org

--------------------------------------------------
--------------------------------------------------
'''




import os
import MySQLdb



def dbSave(name, search) :
	db = MySQLdb.connect(   host="localhost", # your host, usually localhost
				port =3306, # port on which MySQL is running
                     		user="root", # your username
                      		passwd="admin", # your password
                      		db="geeksforgeeks") # name of the database
        cur=db.cursor()
#       cur.execute("SELECT * FROM Records")
	#SQL query to INSERT a record into the table RECORDS.
	cur.execute("INSERT INTO Records (name, search_string) VALUES(%s, %s)", (name, search))

	db.commit()




