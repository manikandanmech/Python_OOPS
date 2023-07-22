                          # Property Method

class student:
    def __init__(self, total):
        self._total = total

    def average(self):
        return self._total / 6.0

    def getter(self):
        return self._total

    def setter(self, t):
        if t < 0 or t > 600:
            print("Invalid Total and can't Change")
        else:
            self._total = t

    total = property(getter, setter)


o = student(550)
print("Total   : ", o.total)
print("Average : ", o.average())
o.total = 450
print("Total   : ", o.total)
print("Average : ", o.average())