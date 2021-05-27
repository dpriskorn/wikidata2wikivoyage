#!/usr/bin/env python3
# License: GPLv3+ (or later)
# Author: Dennis Priskorn

# First find the shelters in WQDS and export them to items.csv using a query like this
# https://query.wikidata.org/#%23%20Public%20baths%20in%20H%C3%A4rn%C3%B6sand%20Municipality%0A%23%20Documentation%20on%20coordinates%3A%20https%3A%2F%2Fen.wikibooks.org%2Fwiki%2FSPARQL%2FWIKIDATA_Precision%2C_Units_and_Coordinates%23Coordinates%0ASELECT%20DISTINCT%20%3Fitem%20%3FitemLabel%20%3FadminLabel%20%3Flat%20%3Flon%20%3Fcoordinates%20%3Fpic%0AWHERE%20%0A%7B%0A%20%20%3Fitem%20wdt%3AP31%20wd%3AQ567998%3B%20%0A%20%20%20%20%20%20%20%20wdt%3AP17%20wd%3AQ34%3B%0A%20%20%20%20%20%20%20%20wdt%3AP131%20wd%3AQ209634%3B%0A%20%20%20%20%20%20%20%20wdt%3AP131%20%3Fadmin%3B%0A%20%20%20%20%20%20%20%20wdt%3AP625%20%3Fcoordinates%3B%0A%20%20%20%20%20%20%20%20p%3AP625%20%3Fcoordinate.%0A%20%3Fcoordinate%20psv%3AP625%20%3Fcoordinate_node.%0A%20%3Fcoordinate_node%20wikibase%3AgeoLongitude%20%3Flon.%0A%20%3Fcoordinate_node%20wikibase%3AgeoLatitude%20%3Flat.%0A%20%20%0A%20%20OPTIONAL%20%0A%20%20%7B%3Fitem%20wdt%3AP18%20%3Fpic.%7D%0A%20%20SERVICE%20wikibase%3Alabel%20%7B%20bd%3AserviceParam%20wikibase%3Alanguage%20%22%5BAUTO_LANGUAGE%5D%2Cen%2Csv%22.%20%7D%0A%7D
# then run this script

import csv
from datetime import datetime

# Example output
# * {{do
# | name=Lomtjärnberget
# | lat=62.588214 | long=17.851131
# | wikidata=Q96578823
# | lastedit=2020-09-23
# }}

with open('items.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print("* {{do")
            print(f"| name={row[1]}")
            print(f"| lat={row[3]} | lon={row[4]}")
            print(f"| wikidata={row[0].replace('http://www.wikidata.org/entity/','')}")
            print(f"| lastedit={datetime.now().strftime('%Y-%m-%d')}")
            print("}}")
            line_count += 1
    print(f'Processed {line_count} lines.')
