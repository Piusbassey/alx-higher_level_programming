#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
words = str.split(',')[2].split()[3:7]
result = ' '.join(words)
print(result + '\n')
