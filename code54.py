class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Snode:
    def __init__(self,data):
        self.data = data
        self.next = None

class link:
    def __init__(self):
        self.head = []
    def next_node(self,data):
        for i in self.head:
            if i.data == data.data:
                return False
        self.head.append(data)
    def search(self,data):
        key = None
        for i in self.head:
            if i.data == data:
                key = i
        return key
    def next_secondary_node(self,n,data):
        key_node = self.search(n)
        while key_node.next != None:
            key_node = key_node.next
        key_node.next = data
    def show_all(self):
        for i in self.head:
            print(f'{i.data} : ',end='')
            while i.next != None:
                i = i.next
                if i != None:
                    print(f'{i.data},',end='')
            print('')

inp = input("input : ").split(",")
l = link()
for i in inp:
    u = i.split(" ")
    if u[0] == "ADN":
        l.next_node(node(u[1]))
    elif u[0] == "ADSN":
        h = u[1].split("-")
        l.next_secondary_node(h[0],Snode(h[1]))
l.show_all()