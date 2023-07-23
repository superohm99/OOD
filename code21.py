def Rshift(num, shift):
    num = int(num) >> int(shift)
    return num

n,s = input("Enter number and shiftcount : ").split()
print(Rshift(int(n),int(s)))