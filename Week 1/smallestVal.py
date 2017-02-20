def findSmall(theList):
    smallVal = 100000000000000
    for i in theList:
        if i < smallVal:
            smallVal = i
    return smallVal
meVals = [12,65,72,88,14,2,42]
# print(findSmall(meVals))
num = findSmall(meVals)
assert(num == 2)
assert(num != 12)
assert(num != 100000000000000)