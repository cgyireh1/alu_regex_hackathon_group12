#!/usr/bin/python3
import re

pattern = r'^@\w+$'

twitter = input("Enter twitter_handle in the format '@username': ")
match = re.match(pattern, twitter)

if match:
    print("pattern matches")

else:
    print("Pattern doesn't match")
