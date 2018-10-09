# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 16:00:00 2018

@author: mvjoshi
"""

# Week 1 - Problem 1    
counter = 0
s = 'azcbobobegghakl'
for i in s:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        counter += 1

print('Number of vowels:', counter)    
# Number of vowels: 5

# Week 1 - Problem 2
counter = 0
for i in range(len(s) - 2):
    if s[i] == 'b' and s[i + 1] == 'o' and s[i + 2] == 'b':
        counter += 1

print ('Number of times bob occurs is:', counter)
# Number of times bob occurs is: 2

# Week 1 - Problem 3
count = 0
maxcount = 0
result = 0
s = 'azcbobobegghakl'
for char in range(len(s) - 1):
    if (s[char] <= s[char + 1]):
        count += 1
        if count > maxcount:
            maxcount = count
            result = char + 1
    else:
        count = 0
startposition = result - maxcount
print('Longest substring in alphabetical order is:', 
      s[startposition:result + 1])
# Longest substring in alphabetical order is: beggh
