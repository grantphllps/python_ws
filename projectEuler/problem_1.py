def isMultiple(x,y,list):
    """Is X a multiple of Y"""
    if (x % y) == 0:
            if (x not in list):
                list.append(x)
                
list = []
max = 1000
min = 1

for i in range(min,max):
    isMultiple(i,3,list)

for j in range(min,max):
    isMultiple(j,5,list)

print(sum(list))