class Car:

    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def __str__(self):
        return "this is a class Car with two attributes color and mileage"

    def txt(self):
        return f"The {self.color} car has {self.mileage} miles"

car1 = Car("blue", "20000")
car2 = Car("red", "30000")

print(car1.txt())
print(car2.txt())
print(car2.__str__())