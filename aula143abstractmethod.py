# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.

from abc import ABC, abstractmethod

class AbstractFoo(ABC):
    def __init__(self, name):
        self._name = name
        self.name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name



class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        print('Isso é inútil')


foo = Foo('Bar')
print(foo.name)