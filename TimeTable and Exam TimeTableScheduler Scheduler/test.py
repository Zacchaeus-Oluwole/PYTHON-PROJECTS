import pandas as pd
# d =  {
#         "Morning\n\n08:00am 09:00am 10:00am 11:00am":[
#                 [4,2,3,4],
#                 ['three','two','three','four'],
#                 ['three','two','three','three'],
#                 [8,2,0,4]
#             ], 
#         "Afternoon\n\n11:30am 12:30pm 01:30pm 02:30pm":[
#                 ['one','three','three','four'],
#                 ['one','two','three','four'],
#                 [1,9,3,4],
#                 [1,9,3,4]
#             ], 
#         "Evening\n\n03:00pm 04:00pm 05:00pm 06:00pm":[
#                 [1,9,'three','four'],
#                 [7,2,3,6],
#                 [1,8,'three','four'],
#                 ['three','two','three','four']
#             ]
#         }

d =  {
        "A":[], 
        "B":[], 
        "C":[]
    }
v = int(input("Enter: "))
b = v//3 + 1
# print(b)
for i in range(0,b):
    d['A'].append([' '])
    # print(type(d['A']))
    d['B'].append([' '])
    d['C'].append([' '])
# m = d["Morning\n\n08:00am 09:00am 10:00am 11:00am"]
# print(m[1][2])

df = pd.DataFrame(d)
# print(d[0:1])
print(df.to_markdown())

# for i in d["Morning\n\n08:00am 09:00am 10:00am 11:00am"]:
#     print(i)
#     for v in i:
#         print(v)

# while True:
#     v = int(input("Enter: "))
#     b = v//3 + 1
#     print(b)