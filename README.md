# get_charts.py

Script to process csv play report from playlist db

## use: get_charts.py <infile.csv>
## writes to: "Charts_YYYY-MM-DD.xlsx"


## Infile is a CSV file with column names counts of plays, structure like:
## Plays, `AlbumTitle`,`TrackTitle`, `TrackArtist`, `Artist`, `AddDate`, `AlbumId`,`Genre`

## CSV Query:

query = SELECT Count(*) as Plays, AlbumTitle, TrackTitle, TrackArtist, Artist, AddDate, AlbumId, Genre
FROM SoundExchangePlaylist
WHERE StartDateTime between '2017-02-28 00:00:01' and NOW()
GROUP BY TrackTitle, AlbumTitle
ORDER BY Plays DESC;

- export as CSV with column titles