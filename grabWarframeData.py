#!/usr/bin/python

import json
import requests
import urllib2
from bs4 import BeautifulSoup
import re
import MySQLdb

#response = requests.get("http://warframe.wikia.com/api/v1/Articles/AsSimpleJson?id=3674")
#print response.status_code
#print response.text

wikia = "http://warframe.wikia.com/wiki/Boltor"
page = urllib2.urlopen(wikia)
extract = BeautifulSoup(page, "html.parser")
foundryTable = extract.find('table', class_='foundrytable')

tableMatch = re.compile('<td rowspan="2"')
titleMatch = re.compile('(title=)"((\w|\s)+)"')
numMatch = re.compile('(<br\/>)(\d+,?\d*)')
for row in foundryTable.findAll("td"):
    if tableMatch.match(str(row)):
        title = str(row)
        print title
        print titleMatch.search(title).group(2)
        print numMatch.search(title).group(2)
#.encode('utf-8')