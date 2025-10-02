class Car:
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return self.brand

firstcar = Car("firstcar")
secondcar = Car("secondcar")
thirdcar = Car("thirdcar")
cars = [firstcar, secondcar, thirdcar]
for i in cars:
    print(i)