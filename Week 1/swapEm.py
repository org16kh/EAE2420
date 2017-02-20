def swapEm(theList, index1, index2):
    tempVal = theList[index1]
    theList[index1]=theList[index2]
    theList[index2]=tempVal
meVals = [12,65,72,88,14,2,42]
swapEm(meVals, 2, 4)

assert(meVals == [12,65,14,88,72,2,42])