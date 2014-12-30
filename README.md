cmdMusic
========

A command line application that downloads and saves files to "path". Made so that I don't have to tediously right click and select "save files as" repetitively.

You can add new sites to scrape by adding a function in databases.py that returns two strings, "link" and "songname" as well as adding the corresponding entries to "dbs" in the main function.

Example Output:
```
Search for music: ratatat loud pipes
100.0% 6605440 / 6605440
Ratatat - Loud Pipes

Search for music:
```
