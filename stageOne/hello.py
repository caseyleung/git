__all__ = ['hello', 'test']


def hello():
    print(f"hello, module")


def test(a, b):
    print(f"return a + b: {a + b}")


def test2(a, b):
    print(f"return a - b: {a - b}")


if __name__ == '__main__':
    test(1, 1)
    print('hi, world')
