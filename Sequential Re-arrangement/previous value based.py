# RE-ARRANGE BY SELECTIVE GROUPING OF DIFFERENT VALUES

x = ['B','B','B','B','D','D','D','D','A','A','A','A','C','C','C','C','E','E','E','E']
l = []
i = 0
v = 1

# RE-ARRANGE BY SELECTIVE GROUPING OF DIFFERENT VALUES---CHECKING THE PAST VALUE
for a in x:
    for b in x:
        if l == []:
            l.append(b)
        elif b != l[-1]:
            l.append(b)
    if len(l) == len(x):
        break

print(x)
print(l)