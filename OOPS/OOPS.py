class Student:
    def __init__(self, name, mark):  # initialization
        self.name_1 = name
        self.mark_1 = mark

    def getData(self):
        self.name_1 = input('enter your name')
        self.mark_1 = input('enter age :')

    def putData(self):
        print(self.name_1, '\n', self.mark_1)


obj = Student('', '')  # creation of object class
obj.getData()
obj.putData()
