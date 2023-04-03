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


def worker_manager():
    w = worker(str)
    w.send(None)
    w.send([(1,), (2,), (3,)])

    print(next(w))
    print(next(w))
    print(next(w))

    w.close()


def worker_senior_manager(f):
    """
    Redirecting work to and from caller and worker
    """
    while True:
        w = worker(f)
        try:
            response_sub_gen = yield from w
        except Exception as e:
            print(f"Ignoring {e.__class__.__name__}")


def demo_quiet_worker():
    qw = worker_senior_manager(str)
    qw.send(None)
    qw.send([(1,), (2,), (3,)])

    print(next(qw))
    print(next(qw))
    print(next(qw))

    qw.close()


if __name__ == '__main__':
    system('clear')
    demo_worker()
    demo_quiet_worker()


# Ref: https://www.youtube.com/watch?v=tmeKsb2Fras&t=632s
