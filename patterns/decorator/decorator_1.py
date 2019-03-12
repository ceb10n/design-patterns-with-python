import abc


class Component(abc.ABC):
    
    @abc.abstractmethod
    def operation(self):
        pass


class Decorator(Component, abc.ABC):
    
    def __init__(self, component):
        self.component = component

    @abc.abstractmethod
    def operation(self):
        pass


class ConcreteComponent(Component):
    
    def operation(self):
        print('Do something from ConcreteComponent')


class ConcreteDecorator(Decorator):

    def operation(self):
        print('Do something decorated')
        self.component.operation()


if __name__ == '__main__':
    component = ConcreteComponent()
    decorator = ConcreteDecorator(component)
    decorator.operation()
