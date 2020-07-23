#!/usr/bin/env python

# created by shuichinet https://gist.github.com/shuichinet
# forked from https://gist.github.com/shuichinet/8159878 21 Nov 2015
# using minor edits by fcrimins https://www.reddit.com/user/fcrimins from https://www.reddit.com/r/google/comments/2xzgyv/remove_duplicate_songs_from_google_play_music/csh6mrh
# also using clever edits by Morgan Gothard https://medium.com/@mgothard
# updated for Python 3.5 by John M. Kuchta https://medium.com/@sebvance 22 Nov 2016 (hey I was busy)
# compiled by John M. Kuchta https://medium.com/@sebvance
# thanks to shuichinet, fcrimins and Mr. Gothard for their work

from gmusicapi import Mobileclient
from getpass import getpass

client = Mobileclient()
logged_in = client.login(input('Username:'), getpass(), Mobileclient.FROM_MAC_ADDRESS)

print('Getting all songs ...')
all_songs = client.get_all_songs()

for song in all_songs:
	song_id = song.get('id')
	timestamp = song.get('recentTimestamp')
	
	if song.get('discNumber') is None:
		discnum = 0
	else:
		discnum = song.get('discNumber')
	
	if song.get('trackNumber') is None:
		tracknum = 0
	else: 
		tracknum = song.get('trackNumber')
	
	key = "%s - %s" % ( song.get('title'), song.get('artist') )
	
	print('	   ' + str(key))