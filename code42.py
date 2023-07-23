class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        return (self.queue.pop(0))
    
    def show(self):
        return (self.queue)

    def size(self):
        return len(self.queue)
    
    def empty(self):
        if len(self.queue) == 0:
            return 1
        return 0

strs = input("Enter people : ")
queue1 = Queue()
queue2 = Queue()
queue3 = Queue()
rou = 1
count = 1
count2 = 1

for i in strs:
    queue1.enqueue(i)


while not queue1.empty():
    # queue2.enqueue(queue1.dequeue())
    if count == 4:
        queue2.dequeue()
        count = 1
    if count2 == 3:
        queue3.dequeue()
        count2 = 1
    if  queue2.size() == 5:
        queue3.enqueue(queue1.dequeue())
    else:
        queue2.enqueue(queue1.dequeue())
    print(rou,end="")
    print(" ",end="")
    print(queue1.show(),end="")
    print(" ",end="")
    print(queue2.show(),end="")
    print(" ",end="")
    print(queue3.show())
    rou+=1
    count+=1
    if (not queue3.empty()):
        count2+=1