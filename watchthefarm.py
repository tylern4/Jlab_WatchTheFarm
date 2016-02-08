#!/usr/bin/env python
from optparse import OptionParser
from getwebpage import *
from bs4 import BeautifulSoup
import json
import time

parser = OptionParser()
parser.add_option("-u", help="jlab username", 
				dest="username",default='')

parser.add_option("-t", "--tape",
                action="store_false", dest="url_type", default=True,
                help="Gets the tape jobs instead of batch jobs")
parser.add_option("-j","--json",
				action="store_true",dest="json_data", default=False,
				help="Save data to JSON format")


(options, args) = parser.parse_args()

if options.url_type:
	url = 'http://scicomp.jlab.org/scicomp/#/auger/jobs'
else:
	url = 'http://scicomp.jlab.org/scicomp/#/jasmine/jobs'

data = get_counts(options.username,getwebpage(url))

if options.json_data:
	with open('data.json', 'a') as file:
		json.dump(data,file,indent=4, separators=(',', ': '))
else:
	print data
