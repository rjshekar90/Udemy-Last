

# 2 stacks using Queue


class stack2Queue:

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, item):
        self.instack.append(item)
        print self.instack

    def dequeue(self):
        while self.instack:
            self.outstack.append(self.instack.pop())

        while self.outstack:
            print  self.outstack.pop(),


q = stack2Queue()
q.enqueue(100)
q.enqueue(200)
q.enqueue(300)

q.dequeue()
