#!/usr/bin/env python



'''
--------------------------------------------------
--------------------------------------------------
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
import MySQLdb
from bs4 import BeautifulSoup
from optparse import OptionParser

import crawler
from crawler import *

import dbconn
from dbconn import *


def parse_options():
  usage = "usage: prog [options] (arg1, arg2, ... argn)"
  parser = OptionParser(usage=usage)
  
  parser.add_option("-t", "--tag", \
		      type="string", \
		      action="store", \
		      dest="inp_tag", \
		      default = "", \
		      help="input tags for downloading from the website")


  parser.add_option("-n", "--name", \
		      type="string", \
		      action="store", \
		      dest="inp_name", \
		      default = "", \
		      help="Enter your name to be stored in the database")
		      
  parser.add_option("-l", "--location", \
		      type="string", \
		      action="store", \
		      dest="inp_location", \
		      default = "/home/yodebu/Desktop/Project/Server/Files", \
		      help="location where downloaded files willl be stored")
		      		      	      
  opts, args = parser.parse_args()
  return opts, args



##-----------------------------------------------------



## enters the search name and Seaerch tag for data analysis




# main function

def main():  
  # parse the input parameters
  opts, args = parse_options()
  Tag = opts.inp_tag
  path = opts.inp_location
  name = opts.inp_name  
  dbSave(name, Tag)  
  ExtractMainLinks(Tag, path)
  


if __name__ == "__main__": main()



