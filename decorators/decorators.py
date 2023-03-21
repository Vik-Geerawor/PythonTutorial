def my_decorator(func):
    def wrapper():
        print(f"Pre-func call")
        # NOTE: function call
        func()
        print(f"Post-func call")
    return wrapper


# say_whee = my_decorator(say_whee)

@my_decorator
def say_whee():
    print("Whee!")


def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


say_whee()
