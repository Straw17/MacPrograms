#!/usr/bin/env python
import webbrowser
import bs4
import requests
print('What is your location?')
place1=input()
print('What is your destination?')
place2=input()
place1.replace(' ', '+')
place2.replace(' ', '+')
webbrowser.open('https://www.google.com/maps/dir/'+place1+'/'+place2+'/')
