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
    
    def __str__(self) -> str:
        p = self.head
        res = ''
        while p != None:
            res += p.value
            res += ' '
            p = p.next
        return res

    def size(self):
        cur, cnt = self.head, 0
        while cur != None:
            cur, cnt = cur.next, cnt + 1
        return cnt

inp = input("Input : ").split(" ")
link_list = LinkedList()
x = inp.pop()
rou = 0
x = x.split("/")
inp.append(x.pop(0))
carry = x.pop()

for i in inp:
    link_list.append(i)
link_list.append(-1)

p = link_list.head
if int(carry) > link_list.size:
    print("Over length")
else:    
    while rou < link_list.size - 1:
        # if rou == link_list.size:
        print(f"Now index {rou} value is {p.value} next value is {p.next.value}")
        rou += int(carry)
        for k in range(0,int(carry)):
            p = p.next




 