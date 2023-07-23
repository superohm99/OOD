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
    
print("******** Parking Lot ********")

m,s,o,n = input("Enter max of car,car in soi,operation : ").split(" ")


m,n = int(m),int(n)
stack = Stack()
for i in s:
    if i.isnumeric() and i != '0':
        stack.push(int(i))

if o == "arrive":
    if n not in stack.set_data:
        if len(stack.set_data) < m:
            print(f"car {n} arrive! : Add Car {n}")
            stack.push(n)
        else:
            print(f"car {n} cannot arrive : Soi Full")
    else:
        print(f"car {n} already in soi")
else:
    if n in stack.set_data:
       stack.set_data.remove(n)
       print(f"car {n} depart ! : Car {n} was remove")
    elif stack.empty():
        print(f"car {n} cannot depart : Soi Empty")
    else:
        print(f"car {n} cannot depart : Dont Have Car {n}")

print(stack.set_data)