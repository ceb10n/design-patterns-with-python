"""Conptual Abstract Factory in Python."""
import abc


class AbstractFactory(abc.ABC):

    @abc.abstractmethod
    def create_product_1(self):
        pass

    @abc.abstractmethod
    def create_product_2(self):
        pass


class AbstractProduct1(abc.ABC):

    @abc.abstractmethod
    def do_something(self):
        pass


class AbstractProduct2(abc.ABC):

    @abc.abstractmethod
    def do_something(self):
        pass


class ConcreteProduct1(AbstractProduct1):

    def do_something(self):
        print('Doing something from Product 1')


class ConcreteProduct2(AbstractProduct2):

    def do_something(self):
        print('Doing something from Product 2')


class ConcreteFactory1(AbstractFactory):

    def create_product_1(self):
        return ConcreteProduct1()

    def create_product_2(self):
        return ConcreteProduct2()


if __name__ == '__main__':
    factory_1 = ConcreteFactory1()
    product_1 = factory_1.create_product_1()
    product_2 = factory_1.create_product_2()
    product_1.do_something()
    product_2.do_something()
