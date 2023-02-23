import csv
class Items:
    all_names = [] #атрибут хранения созданных экземпляров
    discount = 0.85 #атрибут хранения уровня цен

    def __init__(self, name, price, amt):
        '''Фукнция инициализации'''
        self.__name = name
        self.price = price
        self.amt = amt

        Items.all_names.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) >= 10:
            raise Exception('Длина наименования товара превышает 10 символов')
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        i = 0
        with open('items.csv', 'r', encoding='windows-1251') as f:
            data = csv.DictReader(f)
            for i in data:
                name = i['name']
                price = i['price']
                amt = i['quantity']
                return cls(name, price, amt)

    def total_price(self):
        '''функция подсчета общей стоимости товаров'''
        total_price = self.price * self.amt
        return total_price

    def new_price(self):
        '''фукнция подсчета товара со скидкой'''
        self.price = self.price * self.discount
        return self.price

if __name__ == '__main__':
    #item1 = Items("Смартфон", 10000, 3)
    #item2 = Items("Ноутбук", 20000, 5)

    #print(item1.total_price())
    #print(item2.total_price())

    #Items.discount = 0.8
    #item1.new_price()
    #print(item1.price)
    #print(item2.price)

    #print(Items.all_names)
    Items.instantiate_from_csv()  # создание объектов из данных файла
    print(len(Items.all_names))
    item1 = Items.all_names[0]
    print(item1.name)

