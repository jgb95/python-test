import re

file = open('pych3.txt', 'r').read()

match = re.search(r'\w', file)

print match.group()