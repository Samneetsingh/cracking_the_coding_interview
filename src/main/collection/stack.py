from src.main.collection.linkedLists import SinglyLinkedList


class Stack(object):

    def __init__(self):
        self.storage = SinglyLinkedList()

    def pop(self):
        pass

    def push(self, info):
        pass

    def peek(self):
        pass

    def is_empty(self):
        pass


if __name__ == '__main__':
    stk = Stack()
    stk.push(info=1)
    stk.push(info=2)
    stk.push(info=3)
    stk.pop()
