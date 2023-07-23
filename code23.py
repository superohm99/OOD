def odd_even(types, data, mode):
    check = 1
    res_list = []
    res_str = ""
    if types == "L":
        data = data.split()
    if mode == "Even":
        for i in data:
            if check % 2 == 0 :
                if types == "L":
                    res_list.append(i)
                else:
                    res_str +=str(i)
            check +=1
    else:
        for i in data:
            if check % 2 != 0:
                if types == "L":
                    res_list.append(i)
                else:
                    res_str +=str(i)
            check+=1
    if types == "L":
        return res_list
    else:
        return res_str


print("*** Odd Even ***")
types, data, mode = input("Enter Input : ").split(",")
print(odd_even(types, data, mode))