class   Stack:
    def __init__(self):
        self.set_data = []
    
    def push(self, data):
        self.set_data.append(data)
    
    def pop(self):
        return (self.set_data.pop())
    
    def empty(self):
        if len(self.set_data) == 0:
            return 1
        return 0
    def top(self):
        return self.set_data[-1]
    
class   Disk:
    def __init__(self, weight, freq):
        self.weight = weight
        self.freq = freq
    
    def get_weight(self):
        return self.weight
    
    def get_freq(self):
        return self.freq

inputs = input("Enter Input : ").split(",")
stack = Stack()

for i in inputs:
    int1, int2 = i.split(" ")
    disk = Disk(int1, int2)
    Unmatch = True
    while Unmatch:
        if stack.empty():
            stack.push(disk)
            Unmatch = False
        else:
            if int(stack.top().weight) >= int(disk.get_weight()):
                Unmatch = False
                stack.push(disk)
            else:
                print(stack.pop().freq)

