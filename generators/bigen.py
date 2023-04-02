import collections
from os import system


def worker(f):
    tasks = collections.deque()
    value = None
    while True:
        batch = yield value
        print(f"batch = {batch}")
        value = None
        if batch is not None:
            tasks.extend(batch)
        else:
            if tasks:
                args = tasks.popleft()
                print(f"args = {args}")
                value = f(*args)
                # print(f"worker: value type = {type(value)}")


def example_worker():
    w = worker(str)
    w.send(None)
    w.send([(1,), (2,), (3,)])

    print(next(w))
    print(next(w))
    print(next(w))


if __name__ == '__main__':
    system('clear')
    example_worker()

# Ref: https://www.youtube.com/watch?v=tmeKsb2Fras&t=632s
