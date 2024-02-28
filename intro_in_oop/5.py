""" class Wood:

    def __init__(self, species):
        self.species = species


oak = Wood('oak')
print(oak.species) """


class Counter:
    def __init__(self, value=0):
        self.value = max(value, 0)

    def inc(self, delta=1):
        return Counter(self.value + delta)

    def dec(self, delta=1):
        return Counter(self.value - delta)


c = Counter(-42)

print(c.value)
print(c.inc().inc(5).dec(2).value)
