def sumBetweenNum(numA, numB):
    number = 0
    for i in range(numA, numB):
        number += i
    number += numB
    return number


firstNumber = input("please input first number: ")
secondNumber = input("please input second number: ")

answer = sumBetweenNum(int(firstNumber), int(secondNumber))

print(f"Answer is {answer}")
