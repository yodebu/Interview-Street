#!/usr/bin/env python


'''
--------------------------------------------------
--------------------------------------------------
 @ Name:   GeeksForGeeks Article Extractor
 @ Purpose: To download and save articles filed under each and every tag passed as a Parameter mentioned in www.geeksforgeeks.org 
 @ Author: Debapriya Das
 	Dept of CSE, NIT Durgapur

V1.0 - 06.02.2015 - basic implementation

 # MIT License - used for non-commercial purposes, used for college project work
 # Special thanks to - GeeksForGeeks.org

--------------------------------------------------
--------------------------------------------------
'''





import requests
import os
import pdfkit
from bs4 import BeautifulSoup
import saveFile
from saveFile import *


#defines the system proxy settings
#os.environ['http_proxy'] = '172.16.1.11:3128'
#os.environ['https_proxy'] = '172.16.1.11:3128'


def ExtractMainLinks(Tag,path):

	
		newpath = path + "/"+ Tag + "/" 
		if not os.path.exists(newpath):
		  os.mkdir(newpath)
		url = "http://www.geeksforgeeks.org/tag/" + Tag +"/"
		#headers = { 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36' }
		r=requests.get(url)
		data = r.text
		#data = urllib2.urlopen(url).read()
		#data = urllib.urlencode(values)         REMOVED URLLIB2 SUPPORT AND ADDED NEW RESPONSE SUPPORT
		#req = urllib2.Request(url, headers) 
		#response = urllib2.urlopen(req)
		#data = response.read()
		soup = BeautifulSoup(data)
		allLinks = soup.findAll("h2",class_="post-title")
		listofLinks = []
		for link in allLinks:
			mainLink = str(link.findAll("a")[0]).split("<a href=")[1].split('rel="bookmark"')[0].strip('"').split('"')[0]
			listofLinks.append(mainLink)
		Extract_And_Save_Page_Data(listofLinks,newpath,Tag)

	








