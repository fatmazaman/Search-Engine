#test code
url ='http://xkcd.com/353/'
def get_page(url):
	try:
		import urllib
		return urllib.urlopen(url).read()
	except:
	     return ""	
print get_page(url)