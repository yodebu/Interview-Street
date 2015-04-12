#!/usr/bin/env python


'''
--------------------------------------------------
--------------------------------------------------
 @ Module: Savefile to HTML and PDF formats 
 @ Name:   GeeksForGeeks Article Extractor
 @ Purpose: To download and save articles filed under each and every tag passed as a Parameter mentioned in www.geeksforgeeks.org 
 @ Author: Debapriya Das
 	Dept of CSE, NIT Durgapur

V1.0 - 06.04.2015 - depreciated urlib2 for 403 ERROR, started using Requests library

 # MIT License - used for non-commercial purposes, used for college project work
 # Special thanks to - GeeksForGeeks.org

--------------------------------------------------
--------------------------------------------------
'''


import pdfkit
import requests
import codecs
import os

def Extract_And_Save_Page_Data(listofLinks,newpath,i):

	No = 0
	for item in listofLinks:
		r2 = requests.get(item)
		pageData = r2.text
		filePath = newpath +"//" +str(i)+" "+str(No+1)+".html"
		pdfPath = newpath +"//" +str(i)+" "+str(No+1)+".pdf"
		No = No +1
		with codecs.open(filePath,encoding='utf-8', mode='w+') as f:
			f.write(pageData)
		createPdf(filePath, pdfPath)
		
		
		
def createPdf(filePath, pdfPath) :
	
	options = {
    			'encoding': "UTF-8",
    			'no-outline': None
		}
	pdfkit.from_file(filePath, pdfPath, options=options)	
		
		

