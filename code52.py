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
        c = ['<->','>']
        x = c[1]
        if p.value.isnumeric():
            x = c[0]
        while p != None:
            res += p.value
            if p.next:
                res += f' {x} '
            p = p.next
        return res

    def size(self):
        cur, cnt = self.head, 0
        while cur != None:
            cur, cnt = cur.next, cnt + 1
        return cnt

inp = input("Enter the elements of Linked list/group's size: ").split(" ")

link_list = LinkedList()
origin = LinkedList()
x = inp.pop()
rou = 0
x = x.split("/")
inp.append(x.pop(0))
if len(x) == 0:
    x.append('0')
carry = x.pop()

lists = []
lists2 = []
if not carry.isnumeric():
    carry = 0
for i in inp:
    if i != '':
        lists.append(i)
        origin.append(i)
if int(carry) > len(lists):
    print("")
    while lists:
            for j in range(0,len(lists)):
                if lists:
                    lists2.append(lists.pop(0))
            while lists2:
                link_list.append(lists2.pop())
    print(f"Original Linked list: {origin}")
    print(f"Modified Linked list: {link_list}") 
else:
    if len(lists) == 0:
        print("No elements in Linked List ? OK!")

    if (int(carry) <= 0):
        print("Group' size should be greater than 0")


    if int(carry) > 0 and len(lists) != 0:
        print("")
        while lists:
            for j in range(0,int(carry)):
                if lists:
                    lists2.append(lists.pop(0))
            while lists2:
                link_list.append(lists2.pop())
        print(f"Original Linked list: {origin}")
        print(f"Modified Linked list: {link_list}") 