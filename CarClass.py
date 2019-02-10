class Car:

    def __init__(self):
        self.year = 0
        self.make = "Default"
        self.model = ""
        self.damage = ""
        self.bid = ""
        self.image = ""
        self.url = ""

    def qualify_make(self):
        return {
            'Jeep': lambda: 1,
            'Toyota': lambda: 0.875,
            'Honda': lambda: 0.75,
            'Mitsubishi': lambda: 0.625,
            'Mazda': lambda: 0.5,
            'Ford': lambda: 0.375,
            'Nissan': lambda: 0.25,
        }.get(self.make, lambda: 0.125)()

    def qualify_model(self):
        return {
            'Rogue': lambda: 0.6875,
            '4Runner': lambda: 1,
            'Pathfinder': lambda: 0.75,
            'Murano': lambda: 0.5,
            'Rav4': lambda: 0.9375,
            'C-RV': lambda: 0.875,
            'H-RV': lambda: 0.375,
            'Pilot': lambda: 0.4375,
            'Outlander': lambda: 0.3125,
            'Grand Cherokee': lambda: 0.8125,
            'Cherokee': lambda: 0.625,
            'CX-5': lambda: 0.5625,
            'Outlander Sport': lambda: 0.25,
            'Compass': lambda: 0.1875,
            'Escape': lambda: 0.125,
            'Explorer': lambda: 0.0625,
        }.get(self.model, lambda: 0)()

    def qualify_damage(self):
        return{
            'All Over': lambda: 0.4,
            'Side': lambda: 1,
            'Rear End': lambda: 0.8,
            'Front End': lambda: 0.6,
            'Flood': lambda: 0.2
        }.get(self.damage, lambda: 0)()

    def show(self):
        print(str(self.year) + " " + self.make + " " + self.model + " " + self.bid + " " + self.damage + "\n" + self.url)
