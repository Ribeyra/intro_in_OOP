class Wood:
    def __init__(self, species, growth_rate=1):
        self.species = species
        self.growth_rate = growth_rate
        self.height = 0

    def growing(self):
        self.height += 2 * self.growth_rate


class Oak(Wood):
    def __init__(self, species, growth_rate=1):
        super().__init__(species, growth_rate)
        self.height = 1

    def growing(self):
        super().growing()
        super().growing()


Oak_1 = Oak('oak')
Oak_1.growing()
print(Oak_1.height)
