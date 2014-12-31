def get_next_target(page):
	start_link = page.find('<a href=')
	if start_link == -1:
		return None
    start_quate = page.find('"', start_link)
    end_quate = page.find('"', start_quate+1)
    url = page[start_quate+1 :end_quate]
    return url , end_quate 
def print_all_links(page):
	while True:
        url, endpos = get_next_target('Good "Idea" Works')
        if url:
	        print url
	        page = page[endpos:]
        else:
	        break
