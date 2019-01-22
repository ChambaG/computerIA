class Car:

    def __init__(self):
        self.year = 0
        self.make = "Default"
        self.model = ""
        self.damage = ""
        self.bid = 0
        self.image = ""
        self.url = ""

    def show(self):
        print(str(self.year) + " " + self.make + " " + self.damage + " " + str(self.bid) + " " + self.damage + "\n" + self.url)
