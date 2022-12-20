def add(*args):
    total = sum(args)
    print(total)

add(1, 3, 5, 7, 9)

def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add = 6, multiply = 4)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Lexus", model="IS300H")
print(my_car.make)


def all_aboard(a, *args, **kw):
    print(a, args, kw)

# *args is a tuple and **kw is a dict
all_aboard(4, 7, 3, 0, x=10, y=64)