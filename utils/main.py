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
        '''Ограничение длины наименования товара'''
        if len(value) >= 10:
            raise Exception('Длина наименования товара превышает 10 символов')
        else:
            self.__name = value

    @classmethod
    def instantiate_from_csv(cls, file):
        '''Создание экземпляров класса из файла items.csv'''
        item = []
        with open(file, 'r', encoding='windows-1251') as f:
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

    def __repr__(self):
        return f'Item("{self.__name}", {self.price}, {self.amt})'

    def __str__(self):
        return self.__name

class Phone(Items):

    def __init__(self, name, price, amt, num_sims):
        '''Инициализация класса Phone'''
        super().__init__(name, price, amt) #Наслеование из класса Items
        self.num_sims = num_sims

    @property
    def num_sims(self):
        return self._num_sims

    @num_sims.setter
    def num_sims(self, value):
        '''Проверка показателя количества сим-карт'''
        if value <= 0:
            raise ValueError("Количество сим-карт не может быть 0 или меньше 0!")
        self._num_sims = value
    def __add__(self, other):
        '''Сложние количества товара на складе'''
        if isinstance(other, Items):
            return self.amt + other.amt
        else:
            ValueError("Только объекты Phone и Items")


    def __repr__(self):
        return f'Item("{self.name}", {self.price}, {self.amt}, {self.num_sims})'

if __name__ == '__main__':
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    print(phone1)
    print(repr(phone1))
    phone1.num_sims = 0

