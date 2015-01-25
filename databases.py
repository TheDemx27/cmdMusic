from subprocess import Popen, PIPE, STDOUT
import re

def mp3skull(usrSearch, db, browser, songNum):
	browser.open(db)
	searchForm = browser.get_form(action='/search_db.php')
	searchForm['q'].value = usrSearch
	browser.submit_form(searchForm)

	songNames = browser.select('b')
	songName = re.sub('[</b>\s]', '', str(songNames[songNum]))

	songLinks = browser.select('.show1')
	link = re.search('(http).+(.mp3)', str(songLinks)).group(0)

	return (link, songName)

def soundowl(usrSearch, db, browser, songNum):
	browser.open('%ssearch?q=%s' % (db, usrSearch))
	html = str(browser.parsed)
	songNames = browser.select('a.internal')

	songTitle = re.search('(?:internal">).+?(?=</a>)', str(songNames[songNum + 7]))
	songArtist = re.search('(?:internal">).+?(?=</a>)', str(songNames[songNum + 6]))

	songName = '%s - %s' % (songArtist[9:], songTitle[9:])

	songLinks = browser.select('a')
	browser.follow_link(songLinks[9])
	link = re.search('(http).+(.mp3)', str(browser.parsed)).group(0)

	return (link, songName)

def grooveshark(usrSearch, db, browser, songNum):
	slave = Popen(['ruby', 'grooveshark.rb'], stdin=PIPE, stdout=PIPE, stderr=STDOUT)
	
	code = """
	require 'grooveshark'
	client = Grooveshark::Client.new
	session = client.session

	songs = client.search_songs({search})
	song = songs[{num}]
	url = client.get_song_url(song)
	puts(url)

	STDOUT.flush
	""".format(search=usrSearch, num=songNum)

	slave.stdin.write(code)

	while True:
		line = slave.stdout.readline().rstrip()
		if line == '[end]':
			break
