Build a search engine:
1.Find data --> Web Crawler
2.Build An index --> Search Queries
3.Rank Pages --> PageRank

Find data:
##########
string.find('text')
Python Code
page = web content
start_link = page.find('<a href=')
start_quate = page.find('"',start_link)
end_quate = page.find('"', start_quate+1)
url = (start_quate+1:end_quate)