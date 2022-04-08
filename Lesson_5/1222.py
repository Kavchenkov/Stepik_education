def task(number: int):
    """description"""
    a = 1 + 1
    return number

assert task(1) == 1, task(1)


def task2(number: int):
    """description"""
    a = number + 1
    return a

assert task2(2) == 3


if __name__ == '__main__':
    print(task2(2))
