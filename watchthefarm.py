#!/usr/bin/env python
from optparse import OptionParser
from getwebpage import *
from bs4 import BeautifulSoup

parser = OptionParser()
parser.add_option("-u", help="jlab username", 
				dest="username",default='')

parser.add_option("-t", "--tape",
                action="store_false", dest="url_type", default=True,
                help="Gets the tape jobs instead of batch jobs")


(options, args) = parser.parse_args()

if options.url_type:
	url = 'http://scicomp.jlab.org/scicomp/#/auger/jobs'
else:
	url = 'http://scicomp.jlab.org/scicomp/#/jasmine/jobs'

print get_counts(options.username,getwebpage(url))
