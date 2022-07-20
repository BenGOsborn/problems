# Question Description

# Ship Traveller
# Our friend Popeye wants to visit locations A to J via ship.

# He starts at location A on Day 0, and wants to know the quickest way to visit the rest of the locations.

# He has created a timetable of possible ship routes he could use. It contains rows of start_location, start_date, arrival_location, arrival_date.

# Here are a few sample entries:

# B,15,A,16
# D,132,B,136
# G,45,E,49
# ...
# If he was at location B earlier than day 15, he could get to location A on day 16. If he was at location D earlier than day 132, he could get to location B on day 136. If he was at location G earlier than day 45, he could get to location E on day 49.

# Given the entire timetable Popeye created, can you work out the path he would take to visit all locations from A to J that has the earliest arrival time?

# Popeye starts at A and does not need to visit A again
# Popeye can only get on a ship a day after he arrives at that location
# Popeye can go back to a location he has already visited

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'find_shortest_route' function below.
#
# sample timetable_entries:
#   [['A', 1, 'C', 2], ['C', 3, 'B', 5]]
#
# sample return for find_shortest_route:
#   ['A', 'C', 'B']

def is_valid_next(current_entry, next_entry):
    return next_entry[1] > current_entry[3]


def compare_looking_for(path, compared):
    found = set()

    for elem in path:
        if elem[2] != "A":
            found.add(elem[2])

    if len(found) != len(compared):
        return False

    for i in range(len(found)):
        if found not in path:
            return False
        if path not in found:
            return False

    return True


def dfs(start, associations, path, entries, looking_for):
    if compare_looking_for(path, looking_for):
        return True

    if start in associations:
        for i in associations[start]:
            entry = entries[i]
            path.append(entry)

            if dfs(entry[2], associations, path, entries, looking_for):
                return True

            path.pop(-1)

    return False


def find_shortest_route(timetable_entries: list) -> list:
    associations = {}
    looking_for = set()
    start = "A"

    for entry in timetable_entries:
        if entry[3] != start:
            looking_for.add(entry[1])

    for i, entry in enumerate(timetable_entries):
        if entry[0] not in associations:
            associations[entry[0]] = [i]
        else:
            associations[entry[0]].append(i)

    ret_arr = []
    dfs(start, associations, ret_arr, timetable_entries, looking_for)

    return ret_arr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    timetable_entries_count = int(input().strip())

    timetable_entries = []

    for _ in range(timetable_entries_count):
        row = input().split(',')
        row = [r.strip() for r in row]
        timetable_entries.append(
            [row[0], int(row[1]), row[2], int(row[3])]
        )

    result = find_shortest_route(timetable_entries)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
