def binarySearch(theList, numToSearch):
    lo, hi =0, len(theList)-1
    mid =(lo+hi)//2
    while lo <= hi:
        mid = (lo + hi) // 2
        if theList[mid] > numToSearch:
            lo = mid +1
        elif theList[mid] < numToSearch:
            hi = mid -1
        elif theList[mid]== numToSearch:
            return True
    return False

# assert(binarySearch([6],6))
assert(binarySearch([6,99,8,200, 190, 180, 7,4, 5],7))