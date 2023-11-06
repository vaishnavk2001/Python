class vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color


class car(vehicle):
    def __init__(self, wheel, model):
        self.wheel = wheel
        self.model = model

    def details(self):
        self.brand = input('enter the brand : ')
        self.color = input('enter the color : ')

    def n_detail(self):
        self.wheel = int(input('enter num wheels : '))
        self.model = input('enter model : ')

    def display(self):
        print('brand is :', self.brand)
        print('color is :', self.color)
        print('wheel is :', self.wheel)
        print('model is :', self.model)


v1 = car('', '')
v1.details()
v1.n_detail()
v1.display()
