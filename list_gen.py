#!/usr/local/bin/python3
import csv

results = []
with open("dictionaries/happy.csv") as csvfile:
    reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC) # change contents to floats
    for row in reader: # each row is a list
        results.append(row)
    print(results)
