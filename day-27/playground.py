# def add(*args):
#     total = 0
#     print(args)
#     print(type(args))
#     for x in args:
#         total += x
#     return total
#
#
# n_sum = add(3, 47, 5, 6, 8, 4, 2)
# print(n_sum)


# def calculate(n, **kwargs):
#     n += kwargs["add"]
#     n *= kwargs["multiply"]
#     print(n)
#
#
# calculate(2, add=4, multiply=5)

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make="Nissan")
print(my_car.make)
print(my_car.model)






def test(a, *args, **kw):
    print(a, args, kw)


test(1, 2, 2, x=2,y=3)
