import csv
import pprint
from collections import Counter

from openpyxl import Workbook
from openpyxl.compat import range
from openpyxl.utils import get_column_letter


pp = pprint.PrettyPrinter(indent=4)

columns = ["show", "dj", "playtime", "playID", "track",
           "unk", "unk2", "artist", "ID", "album", "label",
           "adddate", "genre"]

genres = ["Unknown", "Bluegrass", "Blues", "Cajun", "Celtic", "Classical", "Country", "Folk", "Gospel", "Hip Hop", "International", "Jazz", "Lounge-Schlock",
			"Modern", "R & B", "Ragtime", "Rap", "Reggae", "Rock", "Soundtrack", "Space", "Spoken Word",
			"Techno", "Zydeco"]

wb = Workbook();

playlist = []
plist2 = []
x = 0

## counts, easier if we get those from mySQL?

with open('SoundExchangePlaylist_03282017.csv', 'rb') as f:
	reader = csv.DictReader(f, fieldnames=columns)
	for row in reader:
		x += 1
		play = { "artist": row['artist'], "albumID": row['ID'], "track": row['track'],
				 "label": row['label'], "addDate": row['adddate'], "genre": row['genre'] }

		valstring = [ row['artist'], row['ID'], row['track'], row['label'], row['adddate'], row['genre'] ]
		pstring = ", ".join(valstring)
		# print pstring
		playlist.append(play)
		plist2.append(pstring)

# print plist2

c = Counter(plist2)


for k, v in c.iteritems():
	if v > 1:
		print v, k

# for p in plist2:
# 	print p
	# pp.pprint(p)
	## count plays
	## artist, albumID, track, label, adddate, genre



print "rows read: ", x

