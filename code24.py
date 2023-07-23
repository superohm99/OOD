def hbd(age):
    pre_age = 0;
    res = 0
    lists = []
    if age % 2 == 0:
        pre_age = 20
    else:
        pre_age = 21
    lists.append(pre_age//10)
    lists.append(pre_age%10)
    for x in range(1,10000):
            if int(lists[0])*x+(lists[1])*1 == age:
                 res = x
    return res

    

year = input("Enter year : ")
if int(year) % 2 == 0:
    pre_age = 20
else:
    pre_age = 21

print(f"saimai is just {pre_age}, in base {hbd(int(year))}!")

