def calculate(n, **kwargs):
    # print(kwargs)

    # for key, value in kwargs.items():
        # print(key)
        # print(value)

    print(n)
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)


# calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.age = kw.get("age")


my_car = Car(make="Nissan", model="GT-5")
print(my_car.model)
print(my_car.age)
