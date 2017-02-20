##Basic Algorithims

##Swap Function
def swap(theList, index1, index2):
    tempVal = theList[index1]
    theList[index1]=theList[index2]
    theList[index2]=tempVal
meVals = [12,65,72,88,14,2,42]
swap(meVals, 2, 4)

assert(meVals == [12,65,14,88,72,2,42])

##Find Smallest Num
def findSmall(theList):
    small = theList[0]
    for i in range(0,len(theList)):
        if small > theList[i]:
            small = theList[i]
    return small

findSmallList = [99, 8, 54, 7, 1, 57]
smallestNum = findSmall(findSmallList)
assert(smallestNum !=99)
for i in findSmallList:
    if i != 1:
        assert(smallestNum != i)
    else:
        break

##Add Nums in List
def addNums(theList):
    total = 0
    for i in theList:
        total +=i
    return total
listTotalArray = [1,2,3,4,5,6,7,8,9,10]
listTotal = addNums(listTotalArray)
assert(listTotal == 55)
listTotalArray = [99, 8, 67, 74, 39]
listTotal = addNums(listTotalArray)
assert(listTotal == 287)

##Fundamental Sorting Algorithms

##Selection Sort
def selectionSort(theList):
    for i in range(len(theList)):
        least = i
        for k in range(i+1, len(theList)):
            if theList[least] > theList[k]:
                least = k
        swap(theList, least, i)

def insertionSort(theList):
    for j in range(1,len(theList)):
        value = theList[j]
        i = j-1
        while i >=0 and theList[i] > value:
            theList[i+1] = theList[i]
            theList[i] = value
            i = i-1

##Programmer

##Code to Test Selection Sort
listtoSelectSort = [99, 8, 67, 74, 39]
selectionSort(listtoSelectSort)
assert(listtoSelectSort ==[8, 39, 67, 74, 99])
selectionSort(listtoSelectSort)
assert(listtoSelectSort ==[8, 39, 67, 74, 99])
listtoSelectSort = [9, 10, 9, 5, 4, 6, 1, 2, 1]
selectionSort(listtoSelectSort)
assert(listtoSelectSort == [1, 1, 2, 4, 5, 6, 9, 9, 10])

##Code to Test InsertionSort
listToInsertionSort = [9, 10, 9, 5, 4, 6, 1, 2, 1]
insertionSort(listToInsertionSort)
assert(listToInsertionSort == [1, 1, 2, 4, 5, 6, 9, 9, 10])
listToInsertionSort = [8, 9, 9, 7, 42, 22, 14, 1, 42, 42, 35]
insertionSort(listToInsertionSort)
assert(listToInsertionSort == [1,7,8,9,9,14,22,35, 42, 42,42])

##The Invariant of both sorts is that every item left of the current position value of i will be sorted

##Google Engineer

#Number to binary
def binPrint(num):
    binArray = []
    numToCalc = num
    while numToCalc>0:
        binArray.append(numToCalc%2)
        numToCalc>>=1
    binArray.reverse()
    binString = ""
    for i in range(len(binArray)):
        binString += str(binArray[i])
    return binString



comp=binPrint(4)
assert(comp == "100")
comp=binPrint(100)
assert(comp == "1100100")
comp=binPrint(129058)
assert(comp == "11111100000100010")

##Add two numbers without using +
def addNums(num1, num2):
    while num2 !=0:
        carry = num1&num2
        num1 = num1^num2
        num2 = carry<<1
    return num1

numsAdded = addNums(100,100)
assert(numsAdded == 200)
numsAdded = addNums(100,0)
assert(numsAdded == 100)

##Multiply without using *
def multNums(num1, num2):
    total = 0
    while(num2!=0):
        if(num2&1):
            total = addNums(total,num1)
        num1<<=1
        num2>>=1
    return total

numsMult = multNums(100,100)
assert(numsMult == 10000)
##Number of bits necessary to store a positive value would be (ln(number)/ln(2)) +1 because binary is based off a log with a base of two. The base conversion of ln allows for us to easily
## figure out how many bits are necessary and the plus one allows for the formula to be rounded down no matter what while still giving the correct number of bits.