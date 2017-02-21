# 50%
# addLast()
# first()
# last()
# 60% - Coder
# find()
# count()
# addFirst()
# 80% - Programmer
# Write a quick sort algorithm. Keep it clean. Keep it simple. Recursive.
# Write tests to beat up your quick sort algorithm.
# Test for sorting a sorted list
# Test for sorting a reversed list
# Test for sorting an unsorted list
# Sort a list of length one.
# Sort a list of length two.
# Sort several lists with arbitrary lengths.
# What else can you come up with?
# 90% - Engineer
# insertBefore()
# insertAfter()
# remove()
# __iter__()
# 100% - Google Engineer
# Write test cases for all functionality in your list. Be sure to test for boundary conditions such as but not limited to:
# Inserting at the end/beginning
# Removing at the end/beginning
# Inserting into an empty list
# Removing from the end/beginning when list only has one node.
# Adding at the begin/end into an empty list.
# What else can you come up with???
# Comment each test thoroughly as to what you are testing for to make it easier on the TAs.


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # Inserts value into a new node
    # after the given node
    def insertAfter(self, node, value):
        currentNode = self.head
        while currentNode:
            if node == currentNode:
                tempNode = currentNode
                tempNext = currentNode.next
                currentNode = node
                currentNode.next = tempNode
                node.next = tempNext

            else:
                currentNode = currentNode.next

    # Inserts value into a new node
    # before the given node
    def insertBefore(self, node, value):
        currentNode = self.head
        previousNode = None
        while currentNode:
            if node == currentNode:
                tempNode = currentNode
                node.next = currentNode
                currentNode.next = tempNode.next
                previousNode.next = node

            else:
                currentNode = currentNode.next
                previousNode = currentNode

    # Adds the given value as the first
    # value in the list
    def addFirst(self, value):
        newNode = Node(value)
        self.tail = newNode


    # Adds the given value as the last
    # value in the list
    def addLast(self, value):
        self.head = Node()

    # Returns the node that contains
    # the given value
    def find(self, value):
        currentNode = self.head
        while currentNode:
            if currentNode.data == value:
                return value
            else:
                currentNode = currentNode.next

    # Removes the given node
    # from the list
    def remove(self, node):
        currentNode = self.head
        lastNode = None
        while currentNode:
            if currentNode == node:
                lastNode.next = currentNode.next

            else:
                lastNode = currentNode
                currentNode = currentNode.next




    # Returns the first node
    def first(self):
        return self.head

    # Returns the last node
    def last(self):
        runner = self.head
        while runner.next:
            runner = runner.next
        return runner


    # Returns the number of items in the list
    def count(self):
        runner = self.head
        count = 0
        while runner.next:
            runner = runner.next
            count += 1
        return count


    # Allows the user to iterate over
    # the values (not the nodes)
    def __iter__(self):
        runner = self.head
        while (runner):
            yield runner.value
            runner = runner.next


