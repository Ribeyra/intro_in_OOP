""" Пробую создать список с внутренней реализацией через словарь """


class CustomList:
    values = {}
    last_index = 0

    def append(self, value):
        if not self.values:
            self.values[0] = value
        else:
            self.last_index += 1
            self.values[self.last_index] = value

    def view_list(self):
        res = f'[{", ".join(map(str, self.values.values()))}]'
        return res

    def view_value(self, index):
        if index not in self.values:
            return 'Index out of list'
        return self.values[index]


l = CustomList()
print(l.view_list())
CustomList.append(l, 2)
l.append(5)
print(l.view_list())
print(l.view_value(5))
print(l.view_value(1))
