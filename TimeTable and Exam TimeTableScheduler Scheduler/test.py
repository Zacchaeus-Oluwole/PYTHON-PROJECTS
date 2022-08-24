import pandas as pd
d =  {
        "A":[
                [1,2,3,4],
                ['one','two','three','four'],
                ['one','two','three','four'],
                [1,2,3,4]
            ], 
        "B":[
                ['one','two','three','four'],
                ['one','two','three','four'],
                [1,2,3,4],
                [1,2,3,4]
            ], 
        "C":[
                [1,2,'three','four'],
                [1,2,3,4],
                [1,2,'three','four'],
                ['one','two','three','four']
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