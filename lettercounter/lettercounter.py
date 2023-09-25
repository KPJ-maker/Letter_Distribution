'''Pratyush and Yonas, I have figured out how to eliminate /n and we need to 
draw a red rectangle outlined in black, first draw a red filled rectangle and then draw a black non-filled rectangle.'''


import stddraw as sd
import random
import stdarray
from collections import Counter


with open('para1.txt') as f:
    text = f.read()
    

dict = {}
for char in text:
    char = char.lower()
    char = char.strip()

    if char in dict:
        dict[char] += 1
    else:
        dict[char] = 1
chart = print(dict)

# sd.setXscale(-5, 27)                                      ''' this if for the graph outline i.e x and y plane'''
# sd.setYscale(-0.1, 1.1)
# sd.show(chart)


# def init(i,y ):
#     #letFreq = [:25]
#     e = ""
#     if e <= 25:
#         if y == 65+ i or y == 97 + i:
            
#             array = [:25]
#             new[e] = stdarray(e,i)
#             i+=1

#             lettercounter = stdarray()
#         e += 1

    

