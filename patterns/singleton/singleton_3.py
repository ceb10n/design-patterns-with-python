from smodule import this_is_like_a_singleton as s1
from smodule import this_is_like_a_singleton as s2


if __name__ == '__main__':
    print(s1 is s2)
