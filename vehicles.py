class Vehicle:
    def __init__(self):
        self.main_color = ""
        self.maximum_occupancy = ""

    def drive(self):
        print("Vroooom!")

class Cessna(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def refuel_tank(self):
      print('hi')
    def drive(self):
      print("Mary West!")

class Tesla(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

    def drive(self):
        print("Zoooooooooooom!")

class Ram(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0
    def drive(self):
      print("Robert Rice!")

    def refuel_tank(self):
      print('HELLLOOOO!')

class BMW(Vehicle):
    def __init__(self):
        self.leather = 0
    def drive(self):
      print("Roxanne West!")

    def leather_true(self):
      print('LEATHER!!')

class Lexus(Vehicle):
    def __init__(self):
        self.doors = 0
    def drive(self):
      print("Daniel West!")

    def number_of_doors(self):
      print('you have 4 doors!!')

modelS = Tesla()
mx410 = Cessna()
mdtie = BMW()
htheh = Lexus()
hello = Ram()

modelS.drive()
mx410.drive()
mdtie.leather_true()
htheh.number_of_doors()
hello.drive()
htheh.drive()
mdtie.drive()