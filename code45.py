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
    
    def top(self):
        return self.queue[0]
    
    def empty(self):
        if len(self.queue) == 0:
            return 1
        return 0

strs = input("Enter width, height, and room: ").split(" ")
queue = Queue()
queue_val = Queue()
lists = []
check_o = False
width = int(strs[0]) - 1
height = int(strs[1]) - 1
maps = strs[2]
error = 1
x = 0
y = 0


maps = maps.split(",")

for i in maps:
    for j in i:
        if j == "F":
            queue.enqueue((x,y))
            queue_val.enqueue(j)
        if j == "O":
            error = 0
        x += 1
    if x != width + 1:
        error = 2
    y += 1
    x = 0

if queue.empty():
    error = 2

if y - 1 != height:
    error = 2

while not queue.empty() and not check_o and error != 2:
    if queue_val.top() in "_F":
        print("Queue: ",end="")
        print([i for i in queue.show()])
        set_xy = queue.dequeue()
        lists.append((set_xy[0],set_xy[1]))
        # print(set_xy[0],set_xy[1])
        if set_xy[1] - 1 >= 0:
            if maps[set_xy[1] - 1][set_xy[0]] in "_O" and (set_xy[0],set_xy[1] - 1) not in queue.show() and (set_xy[0],set_xy[1] - 1) not in lists:
                queue.enqueue((set_xy[0],set_xy[1] - 1))
                lists.append((set_xy[0],set_xy[1] - 1))
                queue_val.enqueue(maps[set_xy[1] - 1][set_xy[0]])
                if maps[set_xy[1] - 1][set_xy[0]] == "O":
                    check_o = True

        if set_xy[0] + 1 <= width:
            if maps[set_xy[1]][set_xy[0] + 1] in "_O" and (set_xy[0] + 1,set_xy[1]) not in queue.show() and (set_xy[0] + 1,set_xy[1]) not in lists:
                queue.enqueue((set_xy[0] + 1,set_xy[1]))
                lists.append((set_xy[0] + 1,set_xy[1]))
                queue_val.enqueue(maps[set_xy[1]][set_xy[0] + 1])
                if maps[set_xy[1]][set_xy[0] + 1] == "O":
                    check_o = True

        if set_xy[1] + 1 <= height :
            if maps[set_xy[1] + 1][set_xy[0]] in "_O" and (set_xy[0],set_xy[1] + 1) not in queue.show() and (set_xy[0],set_xy[1] + 1) not in lists:
                queue.enqueue((set_xy[0],set_xy[1] + 1))
                lists.append((set_xy[0],set_xy[1] + 1))
                queue_val.enqueue(maps[set_xy[1] + 1][set_xy[0]])
                if maps[set_xy[1] + 1][set_xy[0]] == "O":
                    check_o = True
        
        if set_xy[0] - 1 >= 0:
            if maps[set_xy[1]][set_xy[0] - 1] in "_O" and (set_xy[0] - 1,set_xy[1]) not in queue.show() and (set_xy[0] - 1,set_xy[1]) not in lists:
                queue.enqueue((set_xy[0] - 1,set_xy[1]))
                lists.append((set_xy[0] - 1,set_xy[1]))
                queue_val.enqueue(maps[set_xy[1]][set_xy[0] - 1])
                if maps[set_xy[1]][set_xy[0] - 1] == "O":
                    check_o = True

if check_o and error == 0:
    print("Found the exit portal.")

elif error == 1:
    print("Cannot reach the exit portal.")

elif error == 2:
    print("Invalid map input.")
else:
    print("Cannot reach the exit portal.")
    




        

        
    
