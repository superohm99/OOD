class Node:
    def __init__(self, data = None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinked_list:
    def __init__(self, head = None):
        if head is None:
            self.head = self.tail = None
            self.size = 0
        else:
            self.head = head
            t = self.head
            self.size = 1
            while t.next is not None:
                t = t.next
                self.size += 1
            self.tail = t
    
    def add_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def __str__(self) -> str:
        s = ''
        p = self.head
        while p is not None:
            s += str(p.data)
            if p.next != None:
                s += ' -> '
            p = p.next
        return s

    def append(self, data):
        p = Node(data)
        if self.head is None:
            self.head = p
        else:
            t = self.head
            while t.next is not None:
                t = t.next
            t.next = p
            p.prev = t
        self.size += 1
    
    def add_tail(self, data):
        p = Node(data)
        if self.head is None:
            self.head = p


def get_n_digit(num, i):
    return int(('-' if str(num)[0] == '-' else '') + str(num)[-i:])


link_list = DoublyLinked_list()
link_list_cur = DoublyLinked_list()
lists = []
list_set = [[],[],[],[],[],[],[],[],[],[]]
len_max = 0
c_0 = 0
carry = 1
inp = input("Enter Input : ").split(" ")

for i in inp:
    link_list.append(int(i))
    link_list_cur.append(int(i))
    if int(i) == 0:
        c_0 += 1
    if len(i) > len_max:
        if int(i) < 0:
            len_max = len(i) - 1
        else:
            len_max = len(i)

print("------------------------------------------------------------")
if c_0 != link_list.size:
    for i in range(1,len_max+1):
        print(f"Round : {i}")

        # print(link_list)
        for j in range(0,10):
            print(f"{j} : ",end="")
            p = link_list.head
            while p is not None:
                if (abs(p.data) // carry) % 10 == j:  
                    list_set[j].append(p.data)
                p = p.next
            
            def sort_digit(list_num):
                if len(str(list_num)) > i:
                    if str(list_num)[0] == '-':
                        if (int(str(list_num)[-i]) == 0):
                            return int('-'+str(list_num)[-(i-1):])
                        else:
                            return int('-'+str(list_num)[-i:])
                    if (int(str(list_num)[-i]) == 0) and (int(str(list_num)[-i+1]) == 0):
                        return 1
                    return int(str(list_num)[-i:])
                else:
                    return int(str(list_num)[0:])
            list_set[j].sort(key=sort_digit,reverse=True)
                
            for k in list_set[j]:
                print(k,end=" ")
                lists.append(k)
            print("")
        

        list_set = [[],[],[],[],[],[],[],[],[],[]]
        link_list.head = None
    
        if i == len_max:
            lists.sort()
        while lists:
            link_list.append(lists.pop())
        carry = carry * 10
        print("------------------------------------------------------------")
else:
    len_max = 0


print(f"{len_max} Time(s)")
print("Before Radix Sort : ", end="")
print(link_list_cur)
print("After  Radix Sort : ", end="")
print(link_list)