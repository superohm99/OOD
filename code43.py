class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.empty():
            return 0
        return (self.queue.pop(0))
    
    def show(self):
        return (self.queue)

    def size(self):
        return len(self.queue)
    
    def empty(self):
        if len(self.queue) == 0:
            return 1
        return 0

strs = input("input : ").split(",")
queue = Queue()
num = 0
count = 0
count_error = 0
count_error_input = 0
for i in strs:
    if "D" in i:
        num = i.split("D")
        for m in range(0,int(num[1])):
            if queue.dequeue() == 0:
                count_error +=1
    elif "E" in i:
        num = i.split("E")
        for m in range(0,int(num[1])):
            queue.enqueue(f"*{count}")
            count +=1
    else:
        count_error_input+=1
    print(f"Step : {i}")
    if "D" in i:
        print(f"Dequeue : {queue.show()}")
    elif "E" in i:
        print(f"Enqueue : {queue.show()}")
    else:
        print(queue.show())
    print(f"Error Dequeue : {count_error}")
    print(f"Error input : {count_error_input}")
    print("--------------------")
# Step : D3
# Dequeue : []
# Error Dequeue : 3
# Error input : 0
# --------------------

