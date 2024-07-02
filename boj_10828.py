class STACK:
    def __init__(self):
        self.stack = []
        self.top = -1

    def Sinitialize(self):
        self.stack = []
        self.top = -1
    
    def isEmptyStack(self):
        if self.top == -1:
            return True
        else:
            return False
  
    def push(self, val):
        self.stack.append(val)
        self.top += 1

    def pop(self):
        if(self.isEmptyStack()):
            return -1
        else:
            popVal = self.stack[self.top]
            del self.stack[self.top]
            self.top -= 1
            return popVal
        
s = STACK()
Num = int(input())

for i in range(Num):
    Input = input()
    if Input == "pop":
        print(s.pop())
    elif Input == "size":
        print(len(s.stack))
    elif Input =="empty":
        if s.isEmptyStack():
            print(1)
        else:
            print(0)
    elif Input == "top":
        if s.top == -1:
            print(-1)
        else:
            print(s.stack[s.top])
    else:
        Input = Input.split()
        s.push(Input[1])