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

class Custormer:
    def __init__(self, t_queue, t_cof, que):
        self.t_queue = t_queue
        self.t_cof = t_cof
        self.que = que
    
    def show_que(self):
        return self.que

    def show_t_que(self):
        return self.t_queue

    def show_t_cof(self):
        return self.t_cof

print(" ***Cafe***")
strs = input("Log : ").split("/")
time = 0
queue = Queue()
time_make = 0
time_make2 = 0
cus_de = 0
cus_de2 = 0
que_front = 0
que = 1
bar1 = 1
bar2 = 1
col_time = 0
col_time2 = 0
check1 = True
check2 = True
waiting = False
save_wait = 0
save_index = 0

# def takeSecond(elem):
#     k = elem.split(",")
#     return int(k[0])


# strs.sort(key=takeSecond)


for i in strs:
    i = i.split(",")
    queue.enqueue(Custormer(i[0], i[1], que))
    que+=1

while not queue.empty() and time < 30:
    if cus_de:
        a = int(cus_de.show_que())
    if cus_de2:
        b = int(cus_de2.show_que())
    if cus_de and cus_de2:
        if int(cus_de2.show_que()) < int(cus_de.show_que()) and time_make==time_make2:
            tmp = int(cus_de2.show_que())
            b = a
            a = tmp

    if int(time_make) == time and time_make != 0:
        print(f"Time {time_make} customer {a} get coffee")
        bar1 = 1
        if int(queue.size()) != 0 and cus_de != 0:
            if int(time_make) - int(queue.top().show_t_que()) > int(save_wait):
                save_wait = int(time_make) - int(queue.top().show_t_que())
                save_index = int(queue.top().show_que())
                waiting = True

    if int(time_make2) == time and time_make2 != 0:
        print(f"Time {time_make2} customer {b} get coffee")
        bar2 = 1
        if int(queue.size()) != 0 and cus_de2 != 0:
                if int(time_make2) - int(queue.top().show_t_que()) > int(save_wait):
                    save_wait = int(time_make2) - int(queue.top().show_t_que())
                    save_index = int(queue.top().show_que())
                    waiting = True

    
    if int(queue.size()) != 0:
        if bar1 and int(queue.top().show_t_que()) <= int(time_make) and int(queue.top().show_t_que()) <= int(time):
            time_make = int(queue.top().show_t_cof())+time_make
            cus_de = queue.dequeue()
            bar1 = 0
    
    if int(queue.size()) != 0:
        if bar2 and int(queue.top().show_t_que()) <= int(time_make2)  and int(queue.top().show_t_que()) <= int(time):
            time_make2 = int(queue.top().show_t_cof()) + time_make2
            cus_de2 = queue.dequeue()
            bar2 = 0
    if int(queue.size()) != 0:
        if bar1 and int(queue.top().show_t_que()) > int(time_make)  and int(queue.top().show_t_que()) <= int(time):
            time_make = int(queue.top().show_t_cof())+int(queue.top().show_t_que())
            cus_de = queue.dequeue()
            bar1 = 0
    
    if int(queue.size()) != 0:
        if bar2 and int(queue.top().show_t_que()) > int(time_make2) and int(queue.top().show_t_que()) <= int(time):
            time_make2 = int(queue.top().show_t_cof())+int(queue.top().show_t_que())
            cus_de2 = queue.dequeue()
            bar2 = 0

    time +=1

if cus_de:
    a = int(cus_de.show_que())
if cus_de2:
    b = int(cus_de2.show_que())
if cus_de and cus_de2:
    if int(cus_de2.show_que()) < int(cus_de.show_que()) and time_make2 == time:
        tmp = int(cus_de2.show_que())
        b = a
        a = tmp

if time_make == time:
    print(f"Time {time_make} customer {a} get coffee")
    bar1 = 1

if time_make2 >= time:
    print(f"Time {time_make2} customer {b} get coffee")
    bar2 = 1

if waiting:
    print(f"The customer who waited the longest is : {save_index}")
    print(f"The customer waited for {save_wait} minutes")
else:
    print(f"No waiting")


        
