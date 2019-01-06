import abc
import copy


class Prototype(abc.ABC):

    @abc.abstractmethod
    def clone(self):
        pass


class ConcretePrototype(Prototype):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def clone(self):
        print('Returining a clone of a={}, b={}'.format(self.a, self.b))
        return copy.deepcopy(self)

    def __str__(self):
        return 'a={}, b={}'.format(self.a, self.b)


if __name__ == '__main__':
    proto_1 = ConcretePrototype(1, 2)
    proto_2 = ConcretePrototype(3, 4)

    copy_1 = proto_1.clone()
    copy_2 = proto_2.clone()

    print(copy_1)
    print(copy_2)

    print(copy_1 is proto_1)
    print(copy_1 == proto_1)
    print(copy_1.a == proto_1.a)

    print(copy_2 is proto_2)
    print(copy_2 == proto_2)
    print(copy_2.a == proto_2.a)