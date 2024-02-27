class Wood:
    color = 'green'


class Forest(Wood):
    amount = 100


print(Wood.color)
print(Forest.color)

oak = Wood()
oak.weight = 10

print(oak.color)
print(oak.weight)

print(oak.__dict__)
