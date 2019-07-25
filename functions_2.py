#from functions import addTwoNumbers

#import functions

def findTotal(a, b, c, d, e):
    total = a + b + c + d + e
    return total

def findAverage(total):
    avg = total / 5
    return avg

def findGrade(avg):
    if avg < 50:
        return "fail"
    else:
        return "pass"

total = (findTotal(45, 38, 90, 87, 70))
average = (findAverage(total))
grade = (findGrade(average))

print("Total is " + str(total))
print("Average is " + str(average))
print("Grade is " + grade)