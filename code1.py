print("*** Converting hh.mm.ss to seconds ***")
h , m, s = input("Enter hh mm ss : ").split(" ")
result = (int(h)*60*60) + (int(m)*60) + int(s)
#print(f"{h:02}:{m}:{s} = {result:,} seconds".format(int(2)))
if (int(h) >= 60 or int(h) < 0):
    print(f"hh({h}) is invalid!")
elif (int(m) >= 60 or int(m) < 0):
    print(f"mm({m}) is invalid!")
elif (int(s) >= 60 or int(s) < 0):
    print(f"ss({s}) is invalid!")
elif (-1 < int(h) < 60 and -1 < int(m) < 60 and -1 < int(s) < 60):
    print('%02d' % int(h) +':'+ '%02d' % int(m) +':'+'%02d' % int(s) + ' = ' + f'{result:,}'+' seconds')
