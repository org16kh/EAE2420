# #Ordered List of Generated Elements
#
# from random import randint
#
# def genRandom():
#     yield randint(0,100)
#
# def genOrdered(numElements):
#     listElements=[]
#     for i in range(0,numElements):
#         listElements.append(genRandom())
#     running = True
#     while running:
#         running = False
#         for i in range(len(listElements)-1):
#             if listElements[i]>listElements[i+1]:
#                 listElements[i],listElements[i+1] = listElements[i+1], listElements[i]
#                 running=True
#     return listElements
#
# for i in genOrdered(10):
#     print(i)
def merge_sort(lst):
    # """Sorts the input list using the merge sort algorithm.
    #
    # >>> lst = [4, 5, 1, 6, 3]
    # >>> merge_sort(lst)
    # [1, 3, 4, 5, 6]
    # """
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    # """Takes two sorted lists and returns a single sorted list by comparing the
    # elements one at a time.
    #
    # >>> left = [1, 5, 6]
    # >>> right = [2, 3, 4]
    # >>> merge(left, right)
    # [1, 2, 3, 4, 5, 6]
    # """
    if not left:
        return right
    if not right:
        return left
    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])
list3 = [45, 93, 2, 56, 15, 75, 90, 59, 20, 31, 35, 62, 89, 47, 7, 23, 5, 92, 17, 69]
assert(merge_sort(list3)==[2, 5, 7, 15, 17, 20, 23, 31, 35, 45, 47, 56, 59, 62, 69, 75, 89, 90, 92, 93])