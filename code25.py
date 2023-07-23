class Wordadd:
    def __init__(self, strinput):
        self.strinput = strinput
        self.word_list = []
        self.state_list = []
        self.word_col = []

    def filter_type(self):
        check_state = 0
        for i in self.strinput:
            for j in i:
                if (j==' '):
                    check_state = 1
                if check_state == 0:
                    self.state_list.append(j)
            check_state = 0

    def process(self):
        check1 = 0
        check2 = 0
        for i in self.strinput:
            strstack = ""
            if len(i) != 1:
                for j in i:
                    if (check1 == 1):
                        strstack +=j
                    if (j==' '):
                        check1 = 1
                check1 = 0
                self.word_list.append(strstack)

    def operation(self):
        datacheck1 = ""
        datacheck2 = ""
        count = 0
        for i in self.state_list:
            if i=='p':
                print(f"'{i} {self.word_list[count]}' is Invalid Input !!!")
                return 0
            if i=='R':
                self.word_col = []
                datacheck1 = ""
                datacheck2 = ""
                print("game restarted")
            elif i=='X':
                if self.state_list[count + 1] != 'R':
                    print(f"'{self.word_list[count]}' -> game over")
            elif i=='P' and datacheck1 == datacheck2:
                datacheck1 = str(self.word_list[count][-2]).lower() + str(self.word_list[count][-1]).lower()
                if count < len(self.word_list) - 1:
                    datacheck2 = str(self.word_list[count + 1][0]).lower() + str(self.word_list[count + 1][1]).lower()
                self.word_col.append(self.word_list[count])
                print(f"'{self.word_list[count]}' -> {self.word_col}")
                count +=1


         

print("*** TorKham HanSaa ***")
inputs = input("Enter Input : ").split(",")
word = Wordadd(inputs)
word.filter_type()
word.process()
word.operation()
