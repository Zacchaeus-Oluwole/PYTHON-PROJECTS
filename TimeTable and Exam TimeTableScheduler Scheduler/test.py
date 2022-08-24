import pandas as pd
import ast
d =  {
        "Morning\n\n08:00am 09:00am 10:00am 11:00am":[
                [4,2,3,4],
                ['three','two','three','four'],
                ['three','two','three','three'],
                [8,2,0,4]
            ], 
        "Afternoon\n\n11:30am 12:30pm 01:30pm 02:30pm":[
                ['one','three','three','four'],
                ['one','two','three','four'],
                [1,9,3,4],
                [1,9,3,4]
            ], 
        "Evening\n\n03:00pm 04:00pm 05:00pm 06:00pm":[
                [1,9,'three','four'],
                [7,2,3,6],
                [1,8,'three','four'],
                ['three','two','three','four']
            ]
        }


df = pd.DataFrame(d)
# print(d[0:1])
print(df.to_markdown())
# d['A'][2] = 6
# print(d)
# d['B'][3] = 8
# print(d)
# print(len(d['A'][:2]))

# import random

# a = random.randint(2,12)

# print(a)
# a -= 2
# print(a)