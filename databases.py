import re

def mp3skull(db, usrsearch, browser):
	browser.open(db)
	searchform = browser.get_form(action='/search_db.php')
	searchform['q'].value = usrsearch
	browser.submit_form(searchform)

	songnames = browser.select('b')
	songname = re.sub('[</b>\s]', '', str(songnames[0]))

	songlinks = browser.select('.show1')
	link = re.search('(http).+(.mp3)', str(songlinks)).group(0)

	return (link, songname)

def soundowl(db, usrsearch, browser):
	browser.open('%ssearch?q=%s' % (db, usrsearch))
	
	songartist = re.search('(?:data-artist=").+?(?=")', str(browser.parsed)).group(0)[13:]
	songtitle = re.search('(?:data-title=").+?(?=")', str(browser.parsed)).group(0)[12:]

	songname = '%s - %s' % (songartist, songtitle)
	
	songlinks = browser.select('a')
	browser.follow_link(songlinks[9])
		
	link = re.search('(http).+(.mp3)', str(browser.parsed)).group(0)
	return (link, songname)