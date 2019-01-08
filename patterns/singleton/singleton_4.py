class _Singleton:

    _instance = None

    def say_hello(self):
        print('Hello from {}'.format(id(self)))


def Singleton():
    if _Singleton._instance is None:
        _Singleton._instance = _Singleton()
    
    return _Singleton._instance


if __name__ == '__main__':
    singleton_1 = Singleton()
    singleton_2 = Singleton()
    singleton_3 = Singleton()

    print(singleton_1 is singleton_2)
    print(singleton_1 is singleton_3)

    singleton_1.say_hello()
    singleton_2.say_hello()
    singleton_3.say_hello()