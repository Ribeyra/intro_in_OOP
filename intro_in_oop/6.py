class Forest:
    def __init__(self, species, amount):
        self.species = species
        self.amount = amount

    @property
    def size(self):
        return f'{self.amount} {self.species}'

    @size.setter
    def size(self, new_value):
        self.amount, self.species = new_value.split(' ')

    @size.deleter
    def size(self):
        print('Сжигаем лес')
        self.amount = None
        self.species = None

    @property
    def fire(self):
        print('Сжигаем лес')
        self.amount = None
        self.species = None


dark_forest = Forest('oak', 200)
print(dark_forest.size)             # 200 oak
dark_forest.amount = 500
print(dark_forest.size)             # 500 oak
dark_forest.size = '250 pine'
print(dark_forest.amount)           # 250
print(dark_forest.species)          # pine
# del dark_forest.size                # Сжигаем лес
# print(dark_forest.amount)           # None
# print(dark_forest.species)          # None
dark_forest.fire                    # Сжигаем лес
print(dark_forest.amount)           # None
print(dark_forest.species)          # None
