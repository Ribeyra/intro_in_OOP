class MultiKeyDict(object):
    """Словареподобный контейнер, позволяющий иметь псевдонимы ключей."""

    def __init__(self, **kwargs):
        """
        Инициализирует контейнер.

        Arguments:
            kwargs — пары "ключ-значение", которые будет содержать
            контейнер сразу после инициализации.

        """
        # BEGIN (write your solution here)
        self.values = kwargs
        self.aliases = {}
        # END

    def __getitem__(self, key):
        """
        Возвращает значение по ключу.

        Arguments:
        - key — один из ключей, связанных со значением.

        """
        # BEGIN (write your solution here)
        if key in self.values:
            return self.values[key]
        return self.values[self.aliases[key]]
        # END

    def __setitem__(self, key, value):
        """
        Сохраняет значение по указанному ключу.

        Изменение затрагивает все псевдонимы ключа. Любой из псевдонимов
        может быть указан в роли ключа.

        Arguments:
            key — ключ, по которому будет сохранено значение,
            value — сохраняемое по указанному ключу значение.

        """
        # BEGIN (write your solution here)
        if key in self.values:
            self.values[key] = value
        self.values[self.aliases[key]] = value
        # END

    def alias(self, **kwargs):
        """
        Добавляет псевдоним(ы) для существующих ключей.

        Arguments:
            kwargs — пары "новый ключ - старый ключ". Все "старые ключи"
            должны уже присутствовать в контейнере.

        """
        # BEGIN (write your solution here)
        new_aliases = {}
        """
        Первый цикл исключает псевдонимы для отстутствующих ключей. Если у нас
        нет ключа "m" ни в словаре со значениями, ни в словаре с псевдонимами,
        нет смысла создавать псевдоним для такого ключа
        """
        for key, value in kwargs.items():
            if value not in self.values and value not in self.aliases:
                print(f'key "{value}" not contained in values or aliases')
            else:
                new_aliases[key] = value
        """
        Второй цикл удаляет элемент из словаря со значениями, в случае, если
        ключ начинает использоваться в качестве псевдонима
        """
        for key in new_aliases.keys():
            if key in self.values:
                self.values.pop(key)
        self.aliases.update(new_aliases)
        """
        Третий цикл проверяет цепочки псевдонимов, в которые были внесены
        изменения
        """
        for key, value in new_aliases.items():
            check = self._check_chain_of_aliases()
            check(key, value)
        # END

    def _check_chain_of_aliases(self):
        """
        Функция для проверки цепочки псевдонимов. В chain_of_aliases собираются
        псевдонимы из цепочки. Если в какой-то момент функция находит
        псевдоним, который уже есть в списке, значит цепочка замкнута сама на
        себя и не указывает на реальное значение. Либо, если значение
        псевдонима не является ключем другого псевдонима, или ключем реального
        значения, такие цепочки, как и замкнутые нужно удалить.
        """
        chain_of_aliases = []

        def inner(key, value):
            if (
                key in chain_of_aliases or
                value not in self.aliases and value not in self.values
            ):
                self._delete_chain_of_aliases(key)
                return
            if value not in self.values:
                chain_of_aliases.append(key)
                key = value
                value = self.aliases[value]
                inner(key, value)
            return
        return inner

    def _delete_chain_of_aliases(self, key):
        """
        Функция для удаления. Замкнутые цепочки удаляет delete_chain_down,
        для удаления обрывков дополнительно используется delete_chain_up
        """
        def delete_chain_down(self, key):
            if self.aliases and key in self.aliases:
                key = self.aliases.pop(key)
                delete_chain_down(self, key)
            return

        def delete_chain_up(self, search_value):
            if self.aliases and search_value in self.aliases.values():
                for key, value in self.aliases.copy().items():
                    if value == search_value:
                        self.aliases.pop(key)
                        delete_chain_up(self, key)
            return

        delete_chain_down(self, key)
        delete_chain_up(self, key)


mkd = MultiKeyDict(x=100, y=[10, 20])
mkd.alias(i='x')
print(mkd.aliases)
""" mkd.alias(j='i')
mkd.alias(k='j')
mkd.alias(a='i', n='m', b='j', c='k')   # key "m" not contained in values or...
print(mkd.aliases)  # {'i': 'x', 'j': 'i', 'k': 'j', 'a': 'i', 'b': 'j'...}
mkd.alias(j='c')
print(mkd.aliases)  # {'i': 'x', 'a': 'i'} """
mkd.alias(j='i')
mkd.alias(i='j')
print(mkd.aliases)  # {}
