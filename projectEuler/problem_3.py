def factors(x):
    list = []
    for i in range(1,x):
        if (x % i == 0):
            list.append(i)
    return list

def isPrime(x):
    for i in range(2,x):
        if (x % i == 0):
            return False
    return  True

factorList = factors(600851475143)
print(factorList)
largest = 2
temp = 2

for j in factorList:
    if isPrime(j) == True:
        largest = j

print(largest)