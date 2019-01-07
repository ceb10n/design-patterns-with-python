import abc


class Target(abc.ABC):

    @abc.abstractmethod
    def do_something(self):
        pass


class Adapter(Target):

    def __init__(self, adaptee):
        self.adaptee = adaptee

    def do_something(self):
        self.adaptee.do_something_else()


class Adaptee:
    
    def do_something_else(self):
        print('Doing something else')


class Client:
    
    def __init__(self, target):
        self._target = target

    def lets_do_it(self):
        self._target.do_something()


if __name__ == '__main__':
    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    client = Client(adapter)

    client.lets_do_it()
