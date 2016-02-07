import sys  
from PyQt4.QtGui import *  
from PyQt4.QtCore import *  
from PyQt4.QtWebKit import * 
from bs4 import BeautifulSoup

class Render(QWebPage):  
  def __init__(self, url):  
    self.app = QApplication(sys.argv)  
    QWebPage.__init__(self)  
    self.loadFinished.connect(self._loadFinished)  
    self.mainFrame().load(QUrl(url))  
    self.app.exec_()  
  
  def _loadFinished(self, result):  
    self.frame = self.mainFrame()  
    self.app.quit()  

def getwebpage(url):
	r = Render(url)  
	html = r.frame.toHtml()
	html = str(html)
	return BeautifulSoup(html, "html.parser")

def get_counts(username,soups):
	counts = {}
	for link in soups.find_all('a'): 
		link = str(link)
		beginning = link.find('username')
		if beginning != -1:
			name = link[beginning+9:]
			if name.find(username) != -1:
				name = name[:-4]
				state = name[name.find("state=")+6:name.find(">")-1]
				count = name[name.find(">")+1:]
				counts[state] = int(count)
	return counts