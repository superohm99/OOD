sets = input("Enter All Bid : ").split(' ')
num_sets = 0
num_high = 0
num_sell = 0
check = 1

def check_num_sell(sets, num_high):
    res = 0
    for i in sets:
        if int(i) > int(res) and int(i) < int(num_high):
            res = i
    return res

def check_double(sets, num_high):
    res = 0
    for i in sets:
        if int(i) == int(num_high):
            res += 1
    if res != 1:
        return (1)
    else:
        return (0)

def check_high(sets):
    high = 0
    for i in sets:
        if int(i) > int(high):
            high = i
    return high
    
for i in sets:
    num_sets += 1
if num_sets == 1:
    print("not enough bidder")
else:
    num_high = check_high(sets)
    for i in sets:
        if (check_double(sets, num_high)):
            print("error : have more than one highest bid")
            break
        if check == num_sets:
            num_sell = check_num_sell(sets, num_high)
            print(f"winner bid is {num_high} need to pay {num_sell}")
            break
        check += 1
