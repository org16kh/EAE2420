meVals = [12,65,72,88,14,2,42]
def addVals(meVals):
    total = 0
    for x in meVals:
        total +=x
    return total
num = addVals(meVals)
assert(num == 295)
