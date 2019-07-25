""""
A > 79
B - 60 to 78
C - 49 to 59
D - 40 to 48
E < 40
program should output the right grade.
"""
#grade = 47
#if grade >= 79:
    #print("Your grade = A.")
#elif grade <= 78:
    #print("Your grade is B.")
""""        if grade <= 59:
            print("Your grade is C.")
            if grade <= 48:
                print("Your grade is D.")
                if grade < 40:
                    print("Your grade is E.")"""

def gradeScore (score):
    if score >= 79:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 49:
        grade = "C"
    elif score >= 40:
        grade = "D"
    else:
        grade = "E"
    return grade
print(gradeScore(99))