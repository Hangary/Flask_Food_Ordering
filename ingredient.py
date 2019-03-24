'''
TODO: 
This is a class used to store ingredients.
'''


class Ingredient(object):

    def __init__(self, name, amount=0):
        self._name = name
        self._amount = amount
        self.__is_soldout()

    def __is_soldout(self):
        self._is_soldout = False if self._amount > 0 else True

    # add or substract from the amount
    def change(self, amount):
        self._amount += amount
        self.__is_soldout()

    # reset the amount
    def reset(self, amount):
        self._amount = amount
        self.__is_soldout()

    @property
    def name(self):
        return self._name

    @property
    def amount(self):
        return self._amount

    @property
    def is_soldout(self):
        return self._is_soldout

    def __str__(self):
        return f"{self._name}: {self._amount}"


if __name__ == "__main__":
    butter = Ingredient("butter")
    tomato = Ingredient("tomato", 10)

    print(butter.name, butter.amount, butter.is_soldout)
    print(butter)

    print(tomato)
    tomato.change(-5)
    print(tomato)
    tomato.reset(10)
    print(tomato)
