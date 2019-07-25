""""
For loop repeats a task until the maximum is reached.
While loop - repeat a statement/code/task until a condition is false.

"""

#print(range(3, 10))

valList = []
#count = 0
for val in range(0, 10):
    valList.append(val)
    #count += 2 #count = count + 1

print(valList)
#print(count)

newList = ["John", "James", "Mary"]
for myVal in newList:
    print(myVal)
valList2 = []
for val in range (0, 10):
    if val%2 == 0:
        valList2.append(val)
print(valList2)

i = 0
while i <= 10:
    print(i)
    i += 1

"""valList3 = [23, 45, 87, 474, 89]
while valList3 = 5:
    print(valList3)
    valList3 += 1"""

i = 1
while i < 6:
    print(i)
    i
    i += 1

for x in range(6):
    print(x)