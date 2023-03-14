from collections import deque


def my_deque():
    """
    Implementing a FIFO queue of guests
    deque allows faster appends and pops from both ends
    """
    queue = deque(["Eric", "John", "Michael"])
    queue.append("Terry")
    queue.append("Graham")

    print(f"Guest List: {queue}")

    print(f"Pop guest: {queue.popleft()}")


if __name__ == '__main__':
    my_deque()
