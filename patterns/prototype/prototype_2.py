import copy


class Prototype:
    pass


if __name__ == '__main__':
    proto = Prototype()
    a_copy = copy.deepcopy(proto)