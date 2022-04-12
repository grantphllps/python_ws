def isEven(x,list):
    if (x % 2 == 0):
        list.append(x)

num1 = 1
num2 = 2
list = [2]

change1 = 1

while(num1 < 4000000 and num2 < 4000000):
    if (change1 == 1):
        change1 = 0
        num1 = num1 + num2
        isEven(num1,list)
    else:
        change1 = 1
        num2 = num1 + num2
        isEven(num2,list)

print(sum(list))