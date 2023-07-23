print("*** Reading E-Book ***")
text, highlight = input("Text , Highlight : ").split(',')
res ='['+highlight+']'
text = list(text)
for i in text:
    if i==highlight:
        i=res
    print(i,end="")
