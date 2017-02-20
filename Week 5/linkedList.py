class Node:
    def __init__(self,value, next = None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def getLastNode(self):
        runner = self.head
        while runner.next:
            runner = runner.next
        return runner

    def addLast(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            self.getLastNode().next = Node(value)

    def insert(selfself, value, targetNodeLocation):
        pass
    def __iter__(self):
        runner = self.head
        while(runner):
            yield runner.value
            runner = runner.next
meLinkedList = LinkedList()
meLinkedList.addLast(5)
meLinkedList.addLast(10)
meLinkedList.addLast(15)

print(meLinkedList.head.value)
print(meLinkedList.head.next.value)
print(meLinkedList.head.next.next.value)
