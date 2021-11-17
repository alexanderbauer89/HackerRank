import re

def hackerrank_tweets(s):
    return re.search(r'(?i)(hackerrank)', s)

def score():
    counter = 0
    for _ in range(int(input())):
        if hackerrank_tweets(input()):
            counter = counter + 1
    return counter

print(score())
