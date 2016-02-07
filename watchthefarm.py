from getwebpage import *
from bs4 import BeautifulSoup
 
#Change the url based on if you want batch or tape jobs 
#Batch Farm
url = 'http://scicomp.jlab.org/scicomp/#/auger/jobs'
#Tape
#url = 'http://scicomp.jlab.org/scicomp/#/jasmine/jobs'

#You can hardcode in your username
#username = ""
username = raw_input('Enter your username: ')

soup = getwebpage(url)

print get_counts(username,soup)
