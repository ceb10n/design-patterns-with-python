def say_hello():
    print('Hello from {}'.format(id(say_hello)))


if __name__ == '__main__':
    print(say_hello())
    print(say_hello())
    print(say_hello())