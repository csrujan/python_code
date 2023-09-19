#collections and pprint

import collections, pprint

with open("textdata/data.txt", "r") as s:
    count = collections.Counter(s.read().upper())
    count_val = pprint.pformat(count)
print(count_val)