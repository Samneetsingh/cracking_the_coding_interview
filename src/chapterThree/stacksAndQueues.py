# Three in One: Describe how you could use a single array to implement three stacks.

def three_in_one():
    pass


# Stack Min: How would you design a stack which,
# in addition to push and pop, has a function min which
# returns the minimum element? Push, pop and min should
# all operate in 0(1) time.

class MinStack(object):

    def __init__(self):
        self.min_stack = list()
        self.length = 0

    def pop(self):
        info = self.min_stack[:self.length][0]
        self.min_stack = self.min_stack[self.length:]
        self.length -= 1
        return info

    # def push(self, info):
    #     if self.length == 0:
    #         self.min_stack.append(info)
    #     if self.length > 0:
    #         top = self.pop()
    #         print(top < info)
    #         if top > info:
    #             self.min_stack.append(info)
    #             self.min_stack.append(top)
    #         else:
    #             self.min_stack.append(top)
    #             self.min_stack.append(info)
    #     self.length += 1

    def push(self, info):
        if self.length <= 0:
            self.min_stack.insert(self.length, info)
        else:
            top = self.pop()
            print(top)
            if top > info:
                self.min_stack.append(info)
                self.min_stack.append(top)
            else:
                self.min_stack.append(top)
                self.min_stack.append(info)
        print(self.min_stack)
        self.length += 1

    def min(self):
        return self.min_stack[self.length - 1]


if __name__ == '__main__':
    stk = MinStack()
    stk.push(2)
    stk.push(1)
    stk.push(5)
    stk.push(3)
    print(stk.pop())
    # stk.push(2)
    # print(stk.min())
    print(stk.min())
