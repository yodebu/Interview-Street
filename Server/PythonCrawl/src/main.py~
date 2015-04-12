#!/usr/bin/env python



'''
--------------------------------------------------
--------------------------------------------------
 @ Module : Main Module 
 @ Name:   GeeksForGeeks Article Extractor
 @ Purpose: To download and save articles filed under each and every tag mentioned in www.geeksforgeeks.org 
 @ Author: Debapriya Das
 	Dept of CSE, NIT Durgapur

V1.0 - 06.02.2015 - basic implementation

 # MIT License - used for non-commercial purposes, used for college project work
 # Special thanks to - GeeksForGeeks.org

--------------------------------------------------
--------------------------------------------------
'''



import os
from bs4 import BeautifulSoup
from optparse import OptionParser

import crawler
from crawler import *

import dbconn
from dbconn import *



#parser to parse and pass arguements into the Program
def parse_options():
  usage = "usage: prog [options] (arg1, arg2, ... argn)"
  parser = OptionParser(usage=usage)
  
  parser.add_option("-t", "--tag", \
		      type="string", \
		      action="store", \
		      dest="inp_tag", \
		      default = "", \
		      help="input search tags for downloading from the website")


  parser.add_option("-n", "--name", \
		      type="string", \
		      action="store", \
		      dest="inp_name", \
		      default = "", \
		      help="Enter your name to be stored in the database")
		      
  parser.add_option("-e", "--email", \
		      type="string", \
		      action="store", \
		      dest="inp_email", \
		      default = "", \
		      help="Enter your email to be stored in the database")
  
  parser.add_option("-l", "--location", \
		      type= "string", \
		      action= "store", \
		      dest= "inp_location", \
		      default = "/home/yodebu/Desktop/Project/Interview-Street/Server/Files/", \
		      help= "location where downloaded files willl be stored, update this according to your directory")
		      		      	      
  opts, args = parser.parse_args()
  return opts, args



##-----------------------------------------------------



## MAIN PROGRAM




# main function

def main():  
  # parse the input parameters
  opts, args = parse_options()
  Tag = opts.inp_tag
  email = opts.inp_email
  path = opts.inp_location
  name = opts.inp_name  
  dbSave(name, email, Tag)  
  ExtractMainLinks(Tag, path)
  


if __name__ == "__main__": main()



