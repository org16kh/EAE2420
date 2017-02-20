##50%

def bubbleSort(theList):
    running = True
    while running:
        running = False
        for i in range(len(theList)-1):
            if theList[i]>theList[i+1]:
                theList[i],theList[i+1] = theList[i+1], theList[i]
                running=True
    return theList

##60%

def any(theList, predicate):
    for i in theList:
        if predicate(i):
            return True
    return False

def all(theList, predicate):
    for i in theList:
        if not predicate(i):
            return False
    return True
def count(theList, predicate):
    count = 0
    for i in theList:
        if predicate(i):
            count +=1
    return count

from random import randint

def genRandom():
    yield randint(0,100)

def genOrdered(numElements):
    lastHighest = 0
    for x in range(numElements):
        nextNum = randint(lastHighest, 100+lastHighest)
        lastHighest = nextNum
        yield nextNum

##80%
def binarySearch(FindNumOrNot):
    daList = []
    numToSearch = 0
    for i in genOrdered(10):
        daList.append(i)
    if FindNumOrNot:
        numToSearch = daList[randint(0,len(daList)-1)]
    lo, hi =0, len(daList)-1
    mid = (lo + hi) // 2
    while lo <= hi:
        mid = (lo + hi) // 2
        if daList[mid] > numToSearch:
            hi = mid - 1
        elif daList[mid] < numToSearch:
            lo = mid + 1
        elif daList[mid]==numToSearch:
            return True
    return False

def where(theList, predicate):
    metList=[]
    for i in theList:
        if predicate(i):
            metList.append(i)
    return metList

def select(theList, transform):
    for i in range(len(theList)):
        theList[i]=transform(theList[i])
    return theList

#A linked list has a pointer to a different item in the list along with the data stored by that position in the list where as a normal list just stores the data in its position

#90%
def mergeSort(theList):
    if len(theList)<=1:
        return theList
    midVal = len(theList) //2
    left = mergeSort(theList[:midVal])
    right = mergeSort(theList[midVal:])
    return merge(left,right)

def merge(left, right):
    if not left:
        return right
    if not right:
        return left
    if left[0]<right[0]:
        return [left[0]]+ merge(left[1:], right)
    print(right[0],left, right[1:])
    return [right[0] + merge(left, right[1:])]

#100%

#Lists im using to test everything
list1 = [92, 36, 67, 94, 62, 22, 44, 81, 63, 68, 13, 55, 85, 75, 87, 50, 22, 23, 61, 2]
list2 = [62, 68, 34, 79, 93, 27, 84, 42, 68, 76, 11, 64, 4, 85, 84, 80, 37, 18, 87, 35]
list3 = [45, 93, 2, 56, 15, 75, 90, 59, 20, 31, 35, 62, 89, 47, 7, 23, 5, 92, 17, 69]
list4 = [4, 4, 4, 4, 5, 4, 4, 4, 4]

#Asserts for Bubble Sort
assert(bubbleSort(list1) == [2, 13, 22, 22, 23, 36, 44, 50, 55, 61, 62, 63, 67, 68, 75, 81, 85, 87, 92, 94])
assert(bubbleSort(list2) == [4, 11, 18, 27, 34, 35, 37, 42, 62, 64, 68, 68, 76, 79, 80, 84, 84, 85, 87, 93])
assert(bubbleSort(list3) == [2, 5, 7, 15, 17, 20, 23, 31, 35, 45, 47, 56, 59, 62, 69, 75, 89, 90, 92, 93])
assert(bubbleSort(list4) == [4, 4, 4, 4, 4, 4, 4, 4, 5])

#Asserts for Any()
assert(any(list1,lambda value : value < 50))
assert(not any(list2, lambda value : value >100))
assert(any(list4, lambda value: value == 5))
#Asserts for all()
assert(all(list3, lambda value : value != 100))
assert(not all(list4, lambda value : value == 4))

#Asserts for count()
assert(count(list1,lambda value : value == value) ==20)
assert(count(list2,lambda value : value >20) == 17)

#assert for genOrdered()
list5=[]
for i in genOrdered(20):
    list5.append(i)
for i in range(len(list5)-1):
    assert(list5[i]<=list5[i+1])
list6=[]
for i in genOrdered(100):
    list6.append(i)
for i in range(len(list6)-1):
    assert(list6[i]<=list6[i+1])
#Assert for Binary Search
assert(binarySearch(True))
assert(not binarySearch(False))


##Assert Where
assert(where(list1,lambda value:value<50)==[2, 13, 22, 22, 23, 36, 44])
assert(where(list2,lambda value:value>100)==[])

##Assert Select
assert(select(list1,lambda value:value+1)==[3, 14, 23, 23, 24, 37, 45, 51, 56, 62, 63, 64, 68, 69, 76, 82, 86, 88, 93, 95])
assert(select(list2,lambda value:value+5)==[9, 16, 23, 32, 39, 40, 42, 47, 67, 69, 73, 73, 81, 84, 85, 89, 89, 90, 92, 98])

list1 = [92, 36, 67, 94, 62, 22, 44, 81, 63, 68, 13, 55, 85, 75, 87, 50, 22, 23, 61, 2]
list2 = [62, 68, 34, 79, 93, 27, 84, 42, 68, 76, 11, 64, 4, 85, 84, 80, 37, 18, 87, 35]

##Assert MergeSort
assert(mergeSort(list3)==[2, 5, 7, 15, 17, 20, 23, 31, 35, 45, 47, 56, 59, 62, 69, 75, 89, 90, 92, 93])

# Write code to demonstrate the use of filter(), map(), and reduce().

filterList =[]
for i in filter(lambda value: value<50,list1):
    filterList.append(i)
filterList=sorted(filterList)
assert(filterList == [2, 13, 22, 22, 23, 36, 44])

mapList = []
for i in map(lambda value:value+5,list2):
    mapList.append(i)
modList = [9, 16, 23, 32, 39, 40, 42, 47, 67, 69, 73, 73, 81, 84, 85, 89, 89, 90, 92, 98]
list2 = sorted(list2)
mapList = sorted(mapList)
for i in range(len(mapList)):
    assert(mapList[i]-5 == list2[i])
    assert(mapList[i]==modList[i])

assert(filter(lambda value:value<50,list1))

from functools import reduce
reduceList =[]
total =reduce((lambda x,y: x+y),list2)
assert(total == 1138)
##Filter() is similar to Where() as they both generate sequences of values that meet the given lambda
##Map() and reduce() are similar to select as they both create sequences of modified values based on the lambda
##Map() will do the exact same thing as select() where as reduce() can only return a single value. The value returned will be the total of the lambda expression.