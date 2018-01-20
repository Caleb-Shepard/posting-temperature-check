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

## Very deep
Sarcasm detection - flag topics and look at the mood surrounding these topics. Think of common sarcastic 
tendencies and phrases to take into account
