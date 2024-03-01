""" Пробую создать список с внутренней реализацией через словарь """


class CustomList:
    def __init__(self, incoming_values={}):
        self.last_index = 0
        self.values = {}
        for value in incoming_values:
            self.values[self.last_index] = value
            self.last_index += 1

    def append(self, *value):
        if len(value) > 1:
            raise TypeError(
                f'list.append() takes exactly one argument '
                f'({len(value)} given)'
            )
        else:
            self.last_index += 1
            self.values[self.last_index] = value[0]

    def __getitem__(self, index):
        if not isinstance(index, int):
            raise TypeError('list indices must be integers or slices')
        elif index < 0 and index < -(self.last_index + 1):
            raise IndexError('list index out of range')
        elif index > self.last_index:
            raise IndexError('list index out of range')
        if index < 0:
            index = (self.last_index + 1) - abs(index)
        return self.values.get(index)

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            raise TypeError('list indices must be integers or slices')
        elif index < 0 and index < -(self.last_index + 1):
            raise IndexError('list index out of range')
        elif index > self.last_index:
            raise IndexError('list index out of range')
        if index < 0:
            index = (self.last_index + 1) - abs(index)
        self.values[index] = value

    def __repr__(self):
        res = f'[{", ".join(map(str, self.values.values()))}]'
        return res

    def view_list(self):
        return self.__repr__()

    def view_value(self, index):
        return self.__getitem__(index)


l = CustomList({'a', 'b'})
print(l)                    # [b, a]
print(l.view_list())        # [b, a]
CustomList.append(l, 2)
# l.append(5, 4) #TypeError: list.append() takes exactly one argument (2 given)
l.append(5)
l.append(3)
l.append(8)
print(l)                    # [a, b, 2, 5, 3, 8]
print(l.view_value(1))      # b
l[1] = 2
print(l[-5])                # 5
