import math
import random
import statistics


def math_demo():
    r = math.cos(math.pi / 4)
    print(f"{r:>0.2f}")


def random_demo():
    fruits = ['apple', 'banana', 'mango']
    a = random.choice(fruits)
    print(a)

    random_numbers = random.sample(range(100), 10)
    print(random_numbers)

    b = random.random()
    print(b)

    c = random.randrange(6)
    print(c)


def stats_demo():
    data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]

    mn = statistics.mean(data)
    print(f"mean: {mn:0.2f}")

    md = statistics.median(data)
    print(f"median: {md:0.2f}")

    v = statistics.variance(data)
    print(f"variance: {v:0.2f}")

    stdev1 = statistics.stdev(data)
    print(f"1st Std Dev: {stdev1:0.2f}")

    stdev2 = statistics.stdev(data, 2)
    print(f"2nd Std Dev: {stdev2:0.2f}")


# math_demo()
# random_demo()
stats_demo()
