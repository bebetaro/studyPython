import sys
sys.setrecursionlimit(100000000)


def sum(start, goal, answer):
    if start > goal:
        return answer
    else:
        answer += start
        start += 1
        return sum(start, goal, answer)


while True:
    start = input("Input first number: ")
    goal = input("Input second number: ")
    answer = 0
    if start < goal:
        break
    else:
        print("please input Second number is bigger than first one")

print(sum(int(start), int(goal), answer))
