class Vehicle:
    def __init__(self):
        self.main_color = ""
        self.maximum_occupancy = ""

    def drive(self):
        print("Vroooom!")

    def turn(self, direction):
      print('')

    def stop(self):
      print("please stop")

class Cessna(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def refuel_tank(self):
      print('hi')
    def drive(self):
      print("Mary West!")
    def stop(self):
      print("PLEASE")

class Tesla(Vehicle):
    def __init__(self):
        self.battery_kwh = 0
    def drive(self):
        print("Zoooooooooooom!")
    def stop(self):
      print("PLEASE STOP")

class Ram(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0
    def drive(self):
      print("Robert Rice!")
    def stop(self):
      print("PLEASE STOP NOW")

    def refuel_tank(self):
      print('HELLLOOOO!')

class BMW(Vehicle):
    def __init__(self):
        self.leather = 0
    def drive(self):
      print("Roxanne West!")

    def leather_true(self):
      print('LEATHER!!')

    def stop(self):
      print("PLEASE STOP NOW PLEASE")

class Lexus(Vehicle):
    def __init__(self):
        self.doors = 0
    def drive(self):
      print("Daniel West!")

    def number_of_doors(self):
      print('you have 4 doors!!')

    def stop(self):
      print("PLEASE STOP NOW PLEASE STOP")


vehicle = Vehicle()
modelS = Tesla()
mx410 = Cessna()
mdtie = BMW()
htheh = Lexus()
hello = Ram()

# lexus = Lexus("lexus")

modelS.drive()
mx410.drive()
mdtie.leather_true()
htheh.number_of_doors()
hello.drive()
htheh.drive()
mdtie.drive()

modelS.stop()
htheh.stop()
vehicle.stop()
mx410.stop()
mdtie.stop()

mdtie.main_color = "red"
print(mdtie.main_color)

hello.stop = "please stop at the next corner"
print(hello.stop)