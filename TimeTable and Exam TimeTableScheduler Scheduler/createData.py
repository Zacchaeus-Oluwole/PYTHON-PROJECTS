# importing pandas as pd
import pandas as pd
import random

# list of department, level, courses
dept = ["MTE", "MEE", "CPE", "EEE","CVE"]
level = [500, 400, 300, 200, 100]
courses = []

numberList = []
deptList = []
levelList = []
coursesList = []


count = 0
counter = 0
lcounter = 0
dcounter = 0

for i in range(100):
    ncounter = i+1

    numberList.append(ncounter)
    lL = levelList.append(level[lcounter])
    dL = deptList.append(dept[dcounter])
    for i in range(10):
        cL = dept[dcounter]+str(int(level[lcounter])+int(i))
        courses.append(cL)
    coursesList.append(list(courses))
    courses = []

    count += 1
    counter += 1

    if (count == 4):
        dcounter += 1
        count = 0

    if counter == 20:
        lcounter += 1
        counter = 0
        dcounter = 0

# A dictionary of lists

dict = {'Number': numberList, "Level": levelList, "Dept": deptList, 'Courses': coursesList,}

df = pd.DataFrame(dict)
df.to_csv('data.csv')
print(df.to_markdown())


# Create courses and Units
cu = set()
units = []
c1 = 0
c2 = 0

for i in df["Courses"]:
    for v in i:
        c1 +=1
        cu.add(v)

cuList = sorted(list(cu))
for i in cuList:
    rand = random.randint(1,3)
    units.append(rand)
cuDict = {"Courses":cuList, "Units":units}

# saving the dataframe
dt = pd.DataFrame(cuDict)
dt.to_csv('coursesUnit.csv')
print(dt.to_markdown())
