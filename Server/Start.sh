#!/usr/bin/env bash 
#lends you some flexibility on different systems


# this is the Script that will run on the Server-side of SSH to connect to the Program 


host = "127.0.0.1"

ssh $host
clear


cd /home/yodebu/Desktop/Project/Server/PythonCrawl/src
clear
echo "Interview Street, powered by GeeksforGeeks "
echo "Hi this is the program for searching GeeksforGeeks for interview questions "
echo
echo "Please Enter your name ?? "
read $name
echo "Please enter your Search String - "
read $tag
./main.py -t $tag -n $name

