#!/usr/bin/python3

import re
pattern = r'^\d{2}\-[a-zA-Z]{3}\-\d{4}$'

date = input("Enter date in the format 'dd-MMM-yyyy': ")
match = re.match(pattern, date)

if match:
    print("pattern matches")

else:
    print("Pattern doesn't match")
