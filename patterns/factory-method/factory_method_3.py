class IPhone:

    def call(self):
        print('Calling from my fancy Iphone')


class Galaxy:

    def call(self):
        print('Calling from my fancy Galaxy')


class CellphoneFactory:

    def __init__(self):
        self.cellphone = self.create()

    def make_some_call(self, number):
        print('Calling {}'.format(number))
        self.cellphone.call()


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
