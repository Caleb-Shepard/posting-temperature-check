#!/bin/python3
#!/(♥_♥)\
import csv
import sys
import os



# -----------------------ａｓｓｉｇｎ ｄｅｆｉｎｉｔｉｏｎｓ----------------------
moods = []

for root, dirs, files in os.walk("./dictionaries/"):  
    for filename in files:

        m = filename[:-5]   #  a mood

        dicty = []  #  words implying the mood m
        with open('dictionaries/' + filename) as csvfile:
            reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
            for row in reader:
                dicty.append(row)

        moods.append([m,dicty[0],0])

moods[0][2] += 1
print(moods[0])

# -------------------------------------------------------------------------------

# iterate through sys.argv[1:*]?
# ^ Nah. Just use the first arg \/
print("Taking the temperature of:")
words = sys.argv[1].split()
for w in words:
    #print("***>%s<***" %w)
    for m in moods:
        if w in m[1]:
            m[2] += 1

for m in moods:
    print("{0} has {1} occurences".format( m[0], m[2]))
# Deep
# antiwords
    # make an antiword list
    # When handling not, just look for antiwords after finding a match
    # (by examining antiword match one word before), then create a deficit
# Deficits
    # create deficits and positives untli the end. Do not act on these until it is finished
