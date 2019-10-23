# Project Euler: Q22
# Finde the total of all the name scores in the file
import re
str = open('p022_names.txt').readlines()
names = sorted(str[0].split(','))

clean = []
for name in names:
    match = re.search(r'^(")(.*)(")$', name)
    if match:
        clean.append(match.group(2))
    else:
        raise("error!")

scoreEvaluate = ['start','A', 'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
totalScore = 0
nameCount = 1
for name in clean:
    singleScore = 0
    chars = []
    chars.extend(name)
    for c in chars:
        singleScore += scoreEvaluate.index(c)
    singleScore *= nameCount
    nameCount += 1
    totalScore += singleScore
print(f"Total score of names: {totalScore}")
