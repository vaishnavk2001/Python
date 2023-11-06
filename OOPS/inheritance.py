class student:
    def __init__(self, name, place):
        self.name = name
        self.place = place

    def getData(self):
        self.name = input('enter the name of the sudent :')
        self.place = input('enter the place : ')


class Hod(student):
    def __init__(self, hname, house):
        self.hname = hname
        self.house = house

    def hget(self):
        self.hname = input('enter hod name :')
        self.house = input('enter hod house : ')

    def putData(self):
        print("student name ",self.name)
        print("student place",self.place)
        print("hod name is ",self.hname)
        print("hod place is ",self.house)


obj = Hod('','')
obj.getData()
obj.hget()
obj.putData()
