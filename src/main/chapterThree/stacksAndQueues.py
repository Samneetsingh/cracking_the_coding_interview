# Three in One: Describe how you could use a single array to implement three stacks.


def three_in_one():
    pass


# Stack Min: How would you design a stack which,
# in addition to push and pop, has a function min which
# returns the minimum element? Push, pop and min should
# all operate in 0(1) time.

class MinStack(object):

    def __init__(self):
        self.storage = list()
        self.minimum = None
        self.top = -1

    def __str__(self):
        representation = ""
        for i in range(len(self.storage)):
            representation += "|{}|\n".format(self.storage[-i])
        return representation

    def pop(self):
        if self.top >= 0:
            self.top -= 1
            self.storage = self.storage[self.top:]

    def push(self, info):
        self.storage.insert(self.top, info)
        self.top += 1

    def min(self):
        return self.minimum


if __name__ == '__main__':
    stk = MinStack()
    stk.push(2)
    stk.push(1)
    stk.push(5)
    stk.push(3)
    print(stk)
    print(stk.pop())
    # stk.push(2)
    # print(stk.min())
    print(stk)
    print(stk.min())
