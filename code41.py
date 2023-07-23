class Queue:
    def __init__(self , data = None):
        if data == None:
            self.data = []
        else:
            self.data = data
    
    def enqueue(self, data):
        self.data.append(data)
    
    def dequeue(self):
        return (self.data.pop(0))
    
    def show(self):
        return (self.data)
    
    def empty(self):
        if len(self.data) == 0:
            return 1
        return 0


strs = input("Enter Input : ").split(",")
queue = Queue()
lists = []
k = 'x'
sp = ', '
count = 0
count1 = 0
count2 = 0
for i in strs:
    for j in i:
        if j == 'E':
            k = j
        if k == 'E':
            if (j.isnumeric()):
                queue.enqueue(int(j))
                for a in queue.show():
                    count +=1;
                    print(str(a),end="")
                    if count != len(queue.data):
                        print(", ",end='')
                print("")
            count = 0
        if j == 'D':
            if queue.empty():
                print("Empty")
            else:
                lists.append(queue.dequeue())
                print(str(lists[-1])+" <- ",end="")
                if not queue.empty():
                    for a in queue.show():
                        count +=1
                        print(str(a),end="")
                        if count != len(queue.data):
                            print(", ",end='')
                    print("")
                    count = 0
                else:
                    print("Empty")

if len(lists) != 0:
    for i in lists:
        count2+=1
        print(str(i),end="")
        if count2 != len(lists):
            print(", ",end='')
else:
    print("Empty",end="")
print(" : ",end="")
count2 = 0
if len(queue.data) == 0:
    print("Empty")
else :
    for i in queue.show():
        count2+=1
        print(str(i),end="")
        if count2 != len(queue.data):
            print(", ",end='')


