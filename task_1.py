""""x = str(input("Input a string:"))

if (x == "yes") or (x == "YES") or (x == "Yes"):
    print("Yes")
else:
    print("No")"""

#task2

""""number1 = int(input("Input a number:"))
number2 = int(input("Input a second number:"))
number3 = int(input("Input a third number:"))

if (number1 >= number2) and (number1 >= number3):
    largest = number1
elif (number2 >= number1) and (number2 >= number3):
    largest = number2
else:
    largest = number3

print("The largest= ", largest)"""

#task3 makes a new list of the first and last elements

""""numberList = [78, 76, 67, 432, 65432]

def listMaker(numberList):
    if len(numberList) >= 2:
        return [numberList[0], numberList[-1]]
    else:
        return [numberList[0]]

newList = listMaker(numberList)
print("This is the new list:", newList)"""

#task4 ask user for a number,even or odd, print out appropriate message.

# fnumber = int(input("Please input any number:"))
#
# def numChecker(fnumber):
#     if (fnumber % 2) == 0:
#         print("Your number is even.")
#         if (fnumber % 4) == 0:
#             print("It is a multiple of 4!!")
#     else:
#         print("Your number is odd.")
#
# numChecker(fnumber)

#task5 print first and last half values of tuple is two lines.

randomNumber = (1)

def halfPrinter(randomNumber):
    length = int(len(randomNumber) / 2)
    if length > 1:
        return str(randomNumber[0:length]) + '\n' + str(randomNumber[length:])
    else:
        return str(randomNumber[0])
    #print("The half size of the tuple is:", length)

print(halfPrinter(randomNumber))