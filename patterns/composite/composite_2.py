class SimpleComposite:

    def __init__(self):
        self.children = set()

    def add(self, component):
        self.children.add(component)

    def remove(self, component):
        self.children.discard(component)

    def do_something(self):
        for child in self.children:
            child.do_something()


class Leaf:

    def do_something(self):
        print('A Leaf doing something')


if __name__ == '__main__':
    comp_1 = SimpleComposite()
    leaf_1 = Leaf()
    leaf_2 = Leaf()

    comp_1.add(leaf_1)
    comp_1.add(leaf_2)

    comp_2 = SimpleComposite()
    comp_3 = SimpleComposite()

    leaf_3 = Leaf()
    leaf_4 = Leaf()
    leaf_5 = Leaf()
    leaf_6 = Leaf()

    comp_2.add(leaf_3)
    comp_2.add(leaf_4)

    comp_3.add(leaf_5)
    comp_3.add(leaf_6)
    comp_2.add(comp_3)
    comp_1.add(comp_2)
    
    comp_1.do_something()
