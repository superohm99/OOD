class   StackCalc:
    def __init__(self):
        self.set_data = []
        
    def push(self, data):
        self.set_data.append(data)
    
    def pop(self):
        return int(self.set_data.pop())
    
    def empty(self):
        if len(self.set_data) == 0:
            return 1
        return 0
    
    def top(self):
        return self.set_data[-1]

    def run(self, inst):
        res = 0
        # set_del = False
        # state = True
        # print(self.set_data)
        for i in inst:
            state = True
            state_push = False
            set_del = False
            while state:
                if i.isnumeric():
                    self.push(i)
                    # print(self.set_data)
                    state = False
                elif i in "+-*/":
                    if i == "+":
                        if not set_del:
                            res = 0
                            res += self.pop()
                        if set_del:
                            res += self.pop()
                            state = False
                            state_push = True
                        if state_push:
                            self.push(res)
                            state_push = False
                        set_del = True
                    elif i == "-":
                        if not set_del:
                            res = self.pop()
                        if set_del:
                            res -= self.pop()
                            state = False
                            state_push = True
                        if state_push:
                            self.push(res)
                            state_push = False
                        set_del = True
                    elif i == "*":
                        if not set_del:
                            res = 1
                            res *= self.pop()
                        if set_del:
                            res *= self.pop()
                            state = False
                            state_push = True
                        if state_push:
                            self.push(res)
                            state_push = False
                        set_del = True
                    elif i == "/":
                        if not set_del:
                            res = self.pop()
                        if set_del:
                            res //= self.pop()
                            state = False
                            state_push = True
                        if state_push:
                            self.push(res)
                            state_push = False
                        set_del = True
                elif i == "DUP" or i == "POP" or i == "PSH":
                    if i == "DUP":
                        self.push(self.top())
                        state = False
                    elif i == "POP":
                        self.pop()
                        state = False
                    elif i == "PSH":
                        pass
                else:
                    return f"Invalid instruction: {i}"
        return 1

    def getValue(self):
        if self.empty():
            return 0
        return self.top()


print("* Stack Calculator *")
arg = input("Enter arguments : ").split(" ")
machine = StackCalc()
output = machine.run(arg)
if output == 1:
    print(machine.getValue())
else :
    print(output)