#!/usr/bin/env python3
# License: GPLv3+ (or later)
# Author: Dennis Priskorn

# First find the shelters in WQDS and export them to campsites.csv, then run this script

import csv
from datetime import datetime

# Example output
# * {{sleep
# | name=Lomtjärnberget
# | lat=62.588214 | long=17.851131
# | wikidata=Q96578823
# | lastedit=2020-09-23
# }}

with open('campsites.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print("* {{sleep")
            print(f"| name={row[1]}")
            print(f"| lat={row[3]} | lon={row[4]}")
            print(f"| wikidata={row[0].replace('http://www.wikidata.org/entity/','')}")
            print(f"| lastedit={datetime.now().strftime('%Y-%m-%d')}")
            print("}}")
            line_count += 1
    print(f'Processed {line_count} lines.')
