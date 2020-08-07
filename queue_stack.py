#----coding:utf-8-----
###two queues==a stack
class Stock:
    def __init__(self):
        self.stackA=[]
        self.stackB=[]
    def push(self,value):
        self.stackA.append(value)
    def pop(self):
        if len(self.stackA)==0:
            return None
        while len(self.stackA)!=1:
            self.stackB.append(self.stackA.pop(0))
        self.stackA,self.stackB=self.stackB,self.stackA
        return self.stackB.pop()

s=Stock()
for i in range(1,8):
    s.push(i)
print(s.pop())


####two stacks====a queue
class Stack:
    def __init__(self):
        self.stackA=[]
        self.stackB=[]
    def push(self,value):
        self.stackA.append(value)
    def pop(self):
        if len(self.stackA)==0 and len(self.stackB)==0:
            return None
        if len(self.stackB)>0:
            return self.stackB.pop()
        while len(self.stackA)>0:
            self.stackB.append(self.stackA.pop())
        return self.stackB.pop()

s=Stack()
for i in range(1,8):
    s.push(i)

print('2222:',s.pop())
s.push(100)
for i in range(9):
    print(s.pop())