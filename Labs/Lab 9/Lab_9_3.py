from Date import *

file = 'birthdays.txt'
file = open(file)

birth = []
for i in file:
    birth.append(i.strip().split(" "))


for j in range(len(birth)):
    new = Date(birth[j][0], birth[j][1], birth[j][2])
    birth[j] = new
    
    

    
    

print(min(birth))
print(max(birth))

months = []
for i in birth:
    months.append(i.month)
j = max(set(months), key=months.count)
print(j)
print(month_names[int(j)])