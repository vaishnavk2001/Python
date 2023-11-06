class A:
    def __init__(self, name, mark, hodname, house):
        self.name = name
        self.mark = mark
        self.hodname = hodname
        self.house = house

    def getData(self):
        self.name = input('enter the name :')


class B(A):
    def putData(self):
        self.mark = input('enter the mark : ')


class C(B):
    def rem(self):
        self.hodname = input('enter hod name : ')
        self.house = input('enter house : ')


class D(C):
    def pdata(self):
        print(self.name)
        print(self.mark)
        print(self.hodname)
        print(self.house)


obj = D('', '', '', '')
obj.getData()
obj.putData()
obj.rem()
obj.pdata()