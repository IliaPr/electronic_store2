import csv
import os
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
        '''Ограничение длины наименования товара'''
        if len(value) >= 10:
            raise Exception('Длина наименования товара превышает 10 символов')
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        #path = os.path.join('utils', 'items.csv')
        '''Создание экземпляров класса из файла items.csv'''
        item = []
        with open('items.csv', 'r', encoding='windows-1251') as f:
            data = csv.DictReader(f)
            for i in data:
                name = i['name']
                price = i['price']
                amt = i['quantity']
                item.append(cls(name, price, amt))
            return item

    @staticmethod
    def is_integer(amt):
        '''Проверка числа на целостность'''
        return int(amt) == float(amt)

    def total_price(self):
        '''функция подсчета общей стоимости товаров'''
        total_price = self.price * self.amt
        return total_price

    def new_price(self):
        '''фукнция подсчета товара со скидкой'''
        self.price = self.price * self.discount
        return self.price

#Items.instantiate_from_csv()  # создание объектов из данных файла
#print(len(Items.all_names))