print("*** Fun with Drawing ***")
num = int(input("Enter input : "))

    
check1 = 0
check2 = 0
rou = num + ((num - 1) * 3)
data_rou = rou
list_data = []
list_data2 = []
rou -= 1
start = 0
for i in range(0,num - 1):
    list_data.append(rou)
    list_data2.append(start)
    start +=2
    rou -= 2
    if start == rou:
        list_data.append(rou)
        list_data2.append(start)
        break
def check_data(num1, num2):
    for i in range(0,num):
        if (list_data2[i]<= num1 <=list_data[i]) and (num2 == list_data2[i] or num2 == list_data[i]):
            return 1
    return 0

def check_possible(check,check2,j,i):
    if( (j <= int(check) <= i and j <= int(check2) <= i) or (check_data(check,check2))):
        return 1
    return 0
rou_step = num - 3
# print(list_data)
# print(list_data2)
for i in range(0,data_rou):
    for j in range(0,data_rou):
        if check_possible(i,j,list_data2[check1],list_data[check2]):
            print("#",end="")
        else:
            print(".",end="")
    if i < (data_rou / 2) - 1:
        if i%2 == 0:
            check2+=1
            check1+=1
        if (check1 == num):
            check1 = 0
            check2 = 0
        # print(i)
    else:
        if i%2 == 1:
            check2-=1
            check1-=1
        if (check1 == -1):
            check1 = num -2
            check2 = num -2
    print("")
