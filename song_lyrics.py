#!/usr/bin/python3
import re

pattern = r'^\[Verse \d+\] .*$'

song_lyrics = input("Enter song in the format '[Verse X] some lyrics': ")
match = re.match(pattern, song_lyrics)

if match:
    print("pattern matches")

else:
    print("Pattern doesn't match")
