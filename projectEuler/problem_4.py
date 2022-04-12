def isPalendrome(input):
    converted = str(input)
    length = len(converted)
    lower = 0
    upper = length - 1
    if (length % 2 != 0):    #odd
        while (upper != lower):
            if (converted[upper] == converted[lower]):
                upper = upper - 1
                lower = lower + 1
            else: 
                return 0
                break
        return 1
    else:                   #even
        while (upper != (lower + 1)):
            if (converted[upper] == converted[lower]):
                upper = upper - 1
                lower = lower + 1
            else: 
                return 0
                break
        if (converted[upper] == converted[lower]):
            return 1
        else:
            return 0

largest_palendrome = 0
temp = 1
for x in range(100,1000):
    for y in range(100,1000):
        temp = x*y
        if (isPalendrome(temp) == 1 and temp > largest_palendrome):
            largest_palendrome = temp

print(largest_palendrome)
