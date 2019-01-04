import abc

class Thing:

    def __init__(self, something=None, anotherthing=None):
        self.something = something
        self.anotherthing = anotherthing

    def __repr__(self):
        return f'<Thing: something={self.something}>'


class Builder(abc.ABC):

    @abc.abstractmethod
    def something(self, value):
        pass

    @abc.abstractmethod
    def anotherthing(self, value):
        pass


class ThingBuilder(Builder):

    def __init__(self):
        self.thing = Thing()

    def something(self, value):
        self.thing.something = value

    def anotherthing(self, value):
        self.thing.anotherthing = value

    def get_thing(self):
        return self.thing


class AThingMaker:

    @staticmethod
    def do_thing():
        builder =  ThingBuilder()
        builder.something(1)
        builder.anotherthing(2)
        
        return builder.get_thing()


if __name__ == '__main__':
    a_thing = AThingMaker.do_thing()
    print(a_thing)
