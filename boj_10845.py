class Queue:
    def __init__(self, max_size = 5):
        self.queue = []

    def enqueue(self, n):
        self.queue.append(n)

    def dequeue(self):
        if len(self.queue) == 0:
            return -1
        else:
            popVal = self.queue[0]
            del self.queue[0]
            return popVal
        
s = Queue()
Num = int(input())

for i in range(Num):
    Input = input()
    if Input == "pop":
        print(s.dequeue())
    elif Input == "size":
        print(len(s.queue))
    elif Input =="empty":
        if len(s.queue) == 0:
            print(1)
        else:
            print(0)
    elif Input == "front":
        if len(s.queue) == 0:
            print(-1)
        else:
            print(s.queue[0])
    elif Input == "back":
        if len(s.queue) == 0:
            print(-1)
        else:
            print(s.queue[len(s.queue)-1])
    else:
        Input = Input.split()
        s.enqueue(Input[1])