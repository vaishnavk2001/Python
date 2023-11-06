class A:
    def __init__(self, sname, splace):
        self.sname = sname
        self.splace = splace

    def getData1(self):
        self.sname = input('enter the student name :')
        self.splace = input('enter the  place : ')


class B:
    def __init__(self, hname, hplace):
        self.hname = hname
        self.hplace = hplace

    def getData2(self):
        self.hname = input('enter the hname : ')
        self.hplace = input('enter the hplace : ')


class C(B, A):
    def pdata(self):
        print('student name :', self.sname)
        print('student place ', self.splace)
        print('hod name ', self.hname)
        print('hod place ', self.hplace)

obj = C('','')
obj.getData1()
obj.getData2()
obj.pdata()