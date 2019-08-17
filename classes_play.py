class Inventory:

    my_items = []

    def __init__(self, items) -> None:
        super().__init__()
        self.items = items
        print('já jsem konstruktor')

    def filled_size(self):
        return len(self.items)

    def __repr__(self) -> str:
        return f'Inventory(items={self._items})'

    def __contains__(self, item):
        return item in self._items

    def loot_inventory(self, another: 'Inventory'):
        self.items += another.items
        another.items = []

    def __iter__(self):
        return iter(self._items)

    @property
    def items(self):
        return self._items.copy()

    @items.setter
    def items(self, other_items):
        self._items = other_items


class LimitedInventory(Inventory):

    def __init__(self, items, max_capacity) -> None:
        self.max_capacity = max_capacity
        super().__init__(items)

    def loot_inventory(self, another: 'Inventory'):
        free_space = self.max_capacity - self.filled_size()
        if another.filled_size() > free_space:
            self.items += another.items[:free_space]
            another.items = another.items[free_space:]
        else:
            self.items += another.items
            another.items = []

    @property
    def items(self):
        return self._items.copy()

    @items.setter
    def items(self, other_items):
        if len(other_items) > self.max_capacity:
            raise Exception('inventory is too small')
        self._items = other_items


if __name__ == '__main__':
    inventory_1 = Inventory([
        'vařečka', 'meč osudu'])
    inventory_2 = LimitedInventory([
        'vařečka', 'meč osudu', '30 zlatek'], 4)
    # print(inventory_1.filled_size(), inventory_1.items)
    # print(inventory_2.filled_size(), inventory_2.items)
    # print(inventory_1)
    # print('přidávám louč')
    # inventory_1.items.append('louč')
    # print('přidávám louč hackem')
    # inventory_1._items.append('louč')
    # # print(inventory_1)
    # # inventory_1.items = []
    # # print(inventory_1)
    # # print('louč' in inventory_1)
    # inventory_1.loot_inventory(inventory_2)
    # print(inventory_1)
    # print(inventory_2)
    # inventory_2.loot_inventory(inventory_1)
    # print(inventory_1)
    # print(inventory_2)
    # for item in inventory_1:
    #     print(item)
    print(inventory_1.my_items)
    print(inventory_2.my_items)

    inventory_1.my_items.append('tvoje itemy')
    print(inventory_1.my_items)
    print(inventory_2.my_items)

