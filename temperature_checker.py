#!(♥_♥)
import csv
import sys

moods = []
moods.append('afraid')
moods.append('alive')
moods.append('angry')
moods.append('confused')
moods.append('depressed')
moods.append('good')
moods.append('happy')
moods.append('helpless')
moods.append('hurt')
moods.append('indifferent')
moods.append('interested')
moods.append('love')
moods.append('open')
moods.append('positive')
moods.append('sad')
moods.append('strong')

print('-------')
print(moods)
print('-------')

# iterate through sys.argv[1:*]?

mood_definitions = []

# -------------------------------------------------------------------------------
# moods[i] is the dictionary name and the elements should be assigned in the loop
count = 0
for i in moods:
    filename = moods[count]
    with open('dictionaries/' + filename + '.csv') as csvfile:
        reader = csv.reader(csvfile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:                          # arbitrary for the time being
            mood_definitions.append(row)
    print(mood_definitions[count])
    count = count + 1
# -------------------------------------------------------------------------------

# iterate through sys.argv[1:*]?

# Deep
# antiwords
    # make an antiword list
    # When handling not, just look for antiwords after finding a match
    # (by examining antiword match one word before), then create a deficit
# Deficits
    # create deficits and positives untli the end. Do not act on these until it is finished
