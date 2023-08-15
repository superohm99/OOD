class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

 

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.head == None:
            self.head = Node(item)
            self.size += 1
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(item)
            self.size +=1
    def check(self, item):
        cur = self.head
        while cur != None:
            if int(cur.value)==int(item):
                return True
            cur = cur.next
        return False
    
    def __str__(self) -> str:
        p = self.head
        res = ''
        while p != None:
            res += p.value
            if p.next:
                res += '->'
            p = p.next
        return res

    def size(self):
        cur, cnt = self.head, 0
        while cur != None:
            cur, cnt = cur.next, cnt + 1
        return cnt



inp = input("Enter input: ").split(" ")
bogi = int(inp[0])
min_start = 100000000
min_fini = 0
tranf = inp[1].split(",")
link_list = LinkedList()
front = []
back = []
f_b = []
link_data =[]
ch_start = 1
count = 1
count_row = 1

for i in tranf:
    i = i.split("-")
    front.append(i[0])
    back.append(i[1])
    f_b.append(int(i[0]))
    # f_b.append(int(i[1]))


for i in tranf:
    i = i.split('-')
    if int(i[0]) < int(min_start) and (str(i[0]) not in back):
        min_start = int(i[0])


for i in range(1,bogi+1):
    if (str(i) not in front) and (str(i) not in back) and int(i) < min_start:
        print(f"{count_row}: ",end="")
        link_list.append(str(i))
        link_data.append(str(i))
        print(link_list)
        count_row +=1
        ch_start +=1
        count+=1
        link_list.head = None


link_list.append(str(min_start))
link_data.append(str(min_start))
min_fini = min_start

while count < int(bogi): 
    while str(min_fini) in front:
        for i in tranf:
            i = i.split('-')
    
            if int(i[0]) == int(min_fini):
               
                link_list.append(i[1])
                link_data.append(i[1])
                count +=1
                min_fini = int(i[1])
    print(f"{count_row}: ",end="")
    print(link_list)
    while link_list.check(min_start) or str(min_start) in back :
        min_start += 1

    link_list.head = None
    min_fini = min_start

    if str(min_fini) not in front and str(min_fini) in back:
        num = 1
        while num <= bogi:
            if str(num) not in link_data and str(num) not in back:
                link_list.append(str(num))
                min_fini = num
                break
            num +=1
    else:
        if str(min_fini) not in link_data:
            link_data.append(str(min_fini))
            link_list.append(str(min_fini))
        if count == bogi - 1:
            count_row +=1
            print(f"{count_row}: ",end="")
            print(link_list)
    count += 1
    count_row +=1

for i in range(1,bogi+1):
    if (str(i) not in front) and (str(i) not in back) and int(i) > min_fini:
        print(f"{count_row}: ",end="")
        link_list.head = None
        link_list.append(str(i))
        link_data.append(str(i))
        print(link_list)
        count_row +=1
        ch_start +=1
        count+=1
        link_list.head = None
        
count_row  -=1
print(f"Number of train(s): {count_row}")


