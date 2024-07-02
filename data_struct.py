# linked list
class LinkedNode:
    def __init__(self, val):
        self.val = val
        self.next =  None

class LinkedList:
    def __init__(self):
        self.head = None

    def initialize(self):
        self.head = None
    
    def LLaddFront(self, value):
        if(self.head == None):
            self.head = LinkedNode(value)
        else:
            second = self.head
            self.head = LinkedNode(value)
            self.head.next = second
    
    def LLaddBack(self, value):
        if(self.head == None):
            self.head = LinkedNode(value)
        else:
            tail = self.head
            while(tail.next != None):
                tail = tail.next
            tail.next = LinkedNode(value)
    
    def LLsearch(self, value):
        crnt_Node = self.head
        while crnt_Node is not None:
            if crnt_Node.val == value:
                return True
            else:
                crnt_Node = crnt_Node.next
        print("Node not found")
        return False
    
    def LLdeleteFront(self):
            if (self.head == None):
                print("there is no Node\n")
            else:
                self.head = self.head.next
    
    def LLdeleteBack(self):
            tail = self.head
            if (tail == None):
                print("there is no Node\n")
            while(tail.next != None):
                tail = tail.next
            tail.next = None


#LL test code
'''
LL = LinkedList()
LL.LLaddFront(1)
LinkedList.LLaddFront(LL, 0)
LinkedList.LLaddBack(LL, 2)
LinkedList.LLaddBack(LL, 3)
print(LL.head.val)
LinkedList.LLdeleteFront(LL)
print(LL.head.val)
if(LinkedList.LLsearch(LL,4)):
    print("yes")
'''

#Stack
class STACK:
    def __init__(self, max_size = 5):
        self.stack = []
        self.top = -1
        self.max = max_size - 1

    def Sinitialize(self):
        self.stack = []
        self.top = -1
    
    def isEmptyStack(self):
        if self.top == -1:
            return True
        else:
            return False

    def isFullStack(self):
        if self.top == self.max:
            return True
        else:
            return False
    
    def push(self, val):
        if(self.isFullStack()):
            print("stack is full!!")
        else:
            self.stack.append(val)
            self.top += 1

    def pop(self):
        if(self.isEmptyStack()):
            print("stack is empty")
        else:
            popVal = self.stack[self.top]
            del self.stack[self.top]
            self.top -= 1
            return popVal

# queue

class Queue:
    def __init__(self, max_size = 5):
        self.queue = []

    def enqueue(self, n):
        self.queue.append(n)

    def dequeue(self):
        if len(self.queue) == 0:
            print("queue is empty!!")
        else:
            popVal = self.queue[0]
            del self.queue[0]
            return popVal
        

# hash table 
#요거는 파이썬 딕셔너리 있는 관계로 그냥 hash 함수만 review index의 1:1 함수

# 나눗셈으로 활용

def divide(a):
    return a % 17

# 문자열의 아스키 코드 합을 index

def asI(string):
    a = 0
    for i in range(len(string)):
        a += ord(string[i])
    return a