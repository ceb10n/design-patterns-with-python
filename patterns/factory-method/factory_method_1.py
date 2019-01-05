import abc


class Product(abc.ABC):

    @abc.abstractmethod
    def do_product_thing(self):
        pass


class RealProduct(Product):

    def do_product_thing(self):
        print('Doing real product thing')


class Factory(abc.ABC):

    def __init__(self):
        self.product = self.create()

    def do_something(self):
        print('Doing something in Factory')
        self.product.do_product_thing()

    @abc.abstractmethod
    def create(self):
        pass


class RealFactory(Factory):

    def __init__(self):
        super(RealFactory, self).__init__()

    def create(self):
        return RealProduct()


if __name__ == '__main__':
    factory = RealFactory()
    factory.do_something()