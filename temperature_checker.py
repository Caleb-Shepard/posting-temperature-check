#!(♥_♥)
import csv

moods[]
moods[0] =  'afraid'
moods[1] =  'alive'
moods[2] =  'angry'
moods[3] =  'confused'
moods[4] =  'depressed'
moods[5] =  'good'
moods[6] =  'happy'
moods[7] =  'helpless'
moods[8] =  'hurt'
moods[9] =  'indifferent'
moods[10] = 'interested'
moods[11] = 'love'
moods[12] = 'open'
moods[13] = 'positive'
moods[14] = 'sad'
moods[15] = 'strong'

# moods[i] is the dictionary name and the elements should be assigned in the loop
for i in moods:
    csv_file = csv.reader(open('dictionaries/' + moods[i] + '.csv'))
    mood_list = dict(csv_file)
