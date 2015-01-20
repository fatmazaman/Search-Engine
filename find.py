# Basic method to find the exact url

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')
start_link = page.find('<a href=')
start_quate = page.find('"',start_link)
end_quate = page.find('"', start_quate+1)
url = page[start_quate+1 :end_quate]
print url






