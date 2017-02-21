def quickSort1(array):
    quickSort2(array, 0, len(array)-1)

def quickSort2(array, low, hi):
    if low<hi:
        p = splitArray(array, low, hi)
        quickSort2(array, low, p-1)
        quickSort2(array, p+1, hi)

def findPivot(array, low, hi):
    mid = (hi + low)//2
    pivot = hi
    if array[low]<array[mid]:
        if array[mid]<array[hi]:
            pivot = mid
    elif array[low]< array[hi]:
        pivot = low
    return pivot

def splitArray(array, low, hi):
    pivot = findPivot(array, low, hi)
    pivotVal = array[pivot]
    array[pivot], array[low]= array[low], array[pivot]
    border = low

    for i in range(low, hi+1):
        if array[i]<pivotVal:
            border += 1
            array[i], array[border]= array[border], array[i]
    array[low],array[border] = array[border], array[low]
    return (border)
