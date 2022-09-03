# valueX = 0
# while True:
#     value = int(input('Enter'))
#     if value == valueX:
#         print("NaN")
#     else:
#         print(valueX)
#     valueX = value

x = ['B','B','B','D','D','D','A','A','A','C','C','C']
l = list()
i = 0
v = 1
for a in x:
    for b in x:
        i+=1
        if i == v*3:
            v+=1
            l.append(b)
    if len(l) == len(x):
        break

print(x)
print(l)

