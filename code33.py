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

data = ""
stack = Stack()
def Push_Token(strs):
    leaf = ["+","-","*","/","^"]
    val_leaf = [3,3,5,5,7]
    valid = True
    res = ""
    while valid:
        if strs.isalpha():
            res += str(strs)
            valid = False
        else:
            if stack.empty():
                stack.push(strs)
                valid = False
            else:
                if strs in leaf and stack.top() not in "({[]})":
                    if val_leaf[leaf.index(stack.top())] < val_leaf[leaf.index(strs)]:
                        stack.push(strs)
                        valid = False
                    else:
                        if val_leaf[leaf.index(stack.top())]  >= val_leaf[leaf.index(strs)]:
                            res += stack.pop()
                            valid = True
                            if stack.empty() or stack.top() in "({[":
                                stack.push(strs)
                                valid = False
                        
                elif ((stack.top() in "({[") or (strs in "({[")) and (strs != ")"):
                    # print("KKs")
                    stack.push(strs)
                    valid = False
                elif strs in ")}]" :
                    while stack.top() not in "({[":
                        res += stack.pop()
                    if stack.top() in "({[":
                        stack.pop()
                    valid = False

    return res

strs = input("Enter Infix : ")

for i in strs:
    data += Push_Token(i)

if not stack.empty() and stack.top() not in "()":
    for j in range(0,len(stack.set_data)):
                data += stack.pop()

print(f"Postfix : {data}")