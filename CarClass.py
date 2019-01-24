class Car:

    def __init__(self):
        self.year = 0
        self.make = "Default"
        self.model = ""
        self.damage = ""
        self.bid = ""
        self.image = ""
        self.url = ""

    def show(self):
        print(str(self.year) + " " + self.make + " " + self.model + " " + self.bid + " " + self.damage + "\n" + self.url)
