from robobrowser import RoboBrowser
from urllib.request import urlretrieve, Request
from urllib.error import HTTPError, URLError
import databases, sys, os

def main():
	clear()

	browser = RoboBrowser(history=False)
	dbs = [('http://soundowl.com/', databases.soundowl), ('http://mp3skull.com/', databases.mp3skull)]
	path = 'C:/Users/Demx/Desktop/%s.mp3'

	while True:
		usrsearch = input('Search for music: ')

		for (db, dbfunc) in dbs:
			try:
				link, songname = dbfunc(db, usrsearch, browser)
				urlretrieve(str(link), path % (songname), reporthook)
				print(songname)
				sys.stderr.write('\n')
				break
			except (HTTPError, AttributeError, URLError):
				pass
		
		# TODO: Make better 'No results...' 

		if songname == 'nosong':
			print('No results...\n')

def reporthook(blocknum, blocksize, totalsize):
	readsofar = blocknum * blocksize
	if totalsize > 0:
		percent = readsofar * 1e2 / totalsize
		s = '\r%5.1f%% %*d / %d' % (percent, len(str(totalsize)), readsofar, totalsize)
		sys.stderr.write(s)
		if readsofar >= totalsize:
			sys.stderr.write('\n')
	else:
		sys.stderr.write('\r100.0%% %d / %d\n' % (readsofar, totalsize))

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
	main()
