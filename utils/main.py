class Items:
    all_names = [] #атрибут хранения созданных экземпляров
    discount = 0.85 #атрибут хранения уровня цен

    def __init__(self, name, price, amt):
        '''Фукнция инициализации'''
        self.name = name
        self.price = price
        self.amt = amt

        Items.all_names.append(self)

    def total_price(self):
        '''функция подсчета общей стоисоти товаров'''
        total_price = self.price * self.amt
        return total_price

    def new_price(self):
        '''фукнция подсчета товара со скидкой'''
        self.price = self.price * self.discount
        return self.price

if __name__ == '__main__':
    item1 = Items("Смартфон", 10000, 3)
    item2 = Items("Ноутбук", 20000, 5)

    print(item1.total_price())
    print(item2.total_price())

    Items.discount = 0.8
    item1.new_price()
    print(item1.price)
    print(item2.price)

    print(Items.all_names)

