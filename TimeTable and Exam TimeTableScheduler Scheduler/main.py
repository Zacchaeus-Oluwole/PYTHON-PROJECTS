# importing pandas as pd
import pandas as pd

# list of name, degree, score
# course = ["MTE", "pankaj", "sudhir", "Geeku"]
dept = ["MTE", "MEE", "CPE", "EEE","CVE"]
level = [500, 400, 300, 200, 100]

numberList = []
deptList = []
levelList = []
coursesList = []
courses = []

count = 0
counter = 0
lcounter = 0
dcounter = 0

for i in range(100):
    ncounter = i+1

    numberList.append(ncounter)
    levelList.append(level[lcounter])
    deptList.append(dept[dcounter])

    count += 1
    counter += 1

    if (count == 4):
        dcounter += 1

        count = 0

    if counter == 20:
        lcounter += 1
        counter = 0
        dcounter = 0


print(numberList)


# dictionary of lists
# dict = {'Name': nme, 'degree': deg, 'score': scr}

dict = {'Number': numberList, "Level": levelList, "Dept": deptList, 'Courses':coursesList}
	
df = pd.DataFrame(dict)

# saving the dataframe
df.to_csv('data.csv')
