from utils.main import Items

class Mix_Lang:
    def __init__(self, name, price, amt):
        self._language = "EN"
        super().__init__(name, price, amt)

    @property
    def language(self):
        return self._language

    def change_lang(self):
        '''Смена зыка'''
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'

class Keyboard(Mix_Lang, Items):
    '''Класс для клавиатуры'''
    pass

if __name__ == '__main__':
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    print(kb)
    print(kb.language)
    kb.change_lang()
    print(kb.language)

