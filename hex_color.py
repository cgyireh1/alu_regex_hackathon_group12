#!/usr/bin/python3

import re
pattern = r'^[#].*\d{6}$'

hex_color = input("Enter date in the format '#XXXXXX': ")
match = re.match(pattern, hex_color)

if match:
    print("pattern matches")

else:
    print("Pattern doesn't match")
