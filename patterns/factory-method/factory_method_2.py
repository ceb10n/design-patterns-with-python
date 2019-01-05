import abc


class Cellphone(abc.ABC):

    @abc.abstractmethod
    def call(self):
        pass


class IPhone(Cellphone):

    def call(self):
        print('Calling from my fancy Iphone')


class Galaxy(Cellphone):

    def call(self):
        print('Calling from my fancy Galaxy')


class CellphoneFactory(abc.ABC):

    def __init__(self):
        self.cellphone = self.create()

    def make_some_call(self, number):
        print('Calling {}'.format(number))
        self.cellphone.call()

    @abc.abstractmethod
    def create(self):
        pass


class SamsungFactory(CellphoneFactory):

    def __init__(self):
        super(SamsungFactory, self).__init__()

    def create(self):
        return Galaxy()


class AppleFactory(CellphoneFactory):

    def __init__(self):
        super(AppleFactory, self).__init__()

    def create(self):
        return IPhone()


if __name__ == '__main__':
    factory = SamsungFactory()
    factory.make_some_call('+55 11 999899999')

    factory = AppleFactory()
    factory.make_some_call('+55 11 999899999')
