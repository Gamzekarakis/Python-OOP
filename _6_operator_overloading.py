class Nokta:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


# iki nokta nesnesi yarat
n1 = Nokta(2, 5)
n2 = Nokta(-1, 4)

print("---- overload oncesi -----")
print(n1)
print(n1.__str__())

# print() -> __str__() metodu getirir.
# defult olarak object'ten gelir


class Nokta(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # __str__() metodunu overload ettik
    def __str__(self):
        return 'Bu bir noktadır. Kooridatları: {0}x{1}'.format(self.x, self.y)


print("----- overload sonrası ------")
n1 = Nokta(2, 5)
print(n1)

print(Nokta.__name__)
