from robobrowser import RoboBrowser
from urllib.request import urlretrieve, Request
from urllib.error import HTTPError, URLError
import databases, sys, os, pygame

def main():
	clear()

	browser = RoboBrowser(history=False)

	dbs = [
	('http://grooveshark.com/#!/', databases.grooveshark),
	('http://soundowl.com/', databases.soundowl),
	('http://mp3skull.com/', databases.mp3skull)
	]

	path = 'C:/Users/Demx/Desktop/%s.mp3'

	while True:
		usrInput = input('Search for music: ')
		usrSearches = usrInput.split("&")
		for usrSearch in usrSearches:
			request(browser, dbs, path, usrSearch)

def request(browser, dbs, path, usrSearch):
	songName = None
	usrSelect = True
	songNum = 0

	for (db, dbfunc) in dbs:
		try:
			while usrSelect = True
				pressed = pygame.key.get_pressed()
				link, songName = dbfunc(usrSearch, db, browser, songNum)
				print(songName)
				if pygame.K_UP in pressed:
					songNum++
				if pygame.K_DOWN in pressed:
					songNum--
				if (pygame.K_RETURN):
					break

			urlretrieve(str(link), path % (songName), reporthook)
			sys.stderr.write('\n')
			break
		except (KeyboardInterrupt), AttributeError, HTTPError, URLError):
			pass

	if songName == None:
		print('No results...\n')

def reporthook(blockNum, blockSize, totalSize):
	readSoFar = blockNum * blockSize

	if totalSize > 0:
		percent = readSoFar * 1e2 / totalSize
		percent = 100 if percent > 100 else percent
		readSoFar = totalSize if readSoFar > totalSize else readSoFar
		sys.stderr.write('\r%5.1f%% %*d / %d' % (percent, len(str(totalSize)), readSoFar, totalSize))
		if readSoFar >= totalSize:
			sys.stderr.write('\n')
	else:
		sys.stderr.write('\r100.0%% %d / %d\n' % (readSoFar, totalSize))

def clear():
	os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == '__main__':
	main()
