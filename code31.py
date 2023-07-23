Paren = input("Enter Input : ")
check1 = 0
check2 = 0
for i in Paren:
    if i == "(" or i == ")":
        check1+=1
    elif i == "[" or i == "]":
        check2+=1
if (check1%2 ==0 and check1 != 0 and check2%2 ==0 and check2 != 0):
    print("Parentheses : Matched ! ! !")
else:
    print("Parentheses : Unmatched ! ! !")