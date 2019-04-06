# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！

input_line = input()
#print(input_line)
point = input_line.split()
#print(point)
for i in range(int(point[0])):
    student = input()
    #print(student)
    check = student.split()
    #print(check)
    check[0] = int(check[0])
    check[1] = int(check[1])
    bl = check[1]*5
    result =check[0]-bl
    if result < 0 :
        result = 0
    #result =input(int(check[0]) - int(check[1]*5))
    #print(result)
    if result >= int(point[1]):
        print(i+1)
    

