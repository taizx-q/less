class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    def drive(self):
        print(f"Mašīna {self.brand} brauc!")


firstcar = Car("bmw", 1999)
secondcar = Car("Moskvich", 1950)

firstcar.drive()
secondcar.drive()