# posting-temperature-check
Guess the emotional connotation of a post given the content of the post.

# TODO

## Shallow
Every word has an individual connotation
Each category get a point if the word is found in the category
Categories with points return as percentage of total emotion in a post
e.g.
    happy = 50
    total = 100
    returns 50% happy
Temperature takes each post into account as equal in importance, regardless of length

## Deep
The file is split into phrases, and every phrase has a connotation, and can have more than one connotation
e.g.
    "I was *not* happy" will tell us that the poster was unhappy. There can be opposite emotions,
    or a point deficit can be created
        happy = -1

## Very Deep
Sarcasm detection - flag topics and look at the mood surrounding these topics. Think of common sarcastic 
tendencies and phrases to take into account. A post may begin happy and end sad, or vice versa. Take the end of the post into higher regard if it is a story when judging temperature.

Attempt to correct spelling errors.

## External Desired Features
Webscrapers to pull posts or articles from web platforms. Analyze sections of the net for overall temperature regarding targeted topics.
