# def printValuesThatAreWorthy(someValues, gauntlet):
#     for value in someValues:
#         if(gauntlet(value)):
#             print(value)
#
# def lessThanFifty(victim):
#     return victim<50
#
# values = [2, 72, 100, 30, 69, 42, 197]
# printValuesThatAreWorthy(values, lessThanFifty)
#
# printValuesThatAreWorthy(values, lambda victim : victim < 50)

from random import randint
def genRandomNumbers(numNumbers):
    for num in range(numNumbers):
        yield randint(0,100)
listnums = genRandomNumbers(123045901823)
for num in listnums:
    print(num)

