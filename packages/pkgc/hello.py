from pkga.hello import greet as ga


def greet():
    print(f"Hello from module c.hello from {__name__}")
    ga()


if __name__ == "__main__":
    ga()
