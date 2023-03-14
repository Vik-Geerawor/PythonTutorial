def dict_demo():
    """
    Usage: storing a value with some key and extracting the value given the key.
    key must be immutable    
    """

    data = {'id': 2, 'name': "Vik", 'email': "vik.geerawor@email.com"}
    print(f"data: {data}")

    data['salary'] = 75000
    print(f"Added salary: {data}")

    data['name'] = "Vik Geerawor"
    print(f"Updated name: {data}")

    keys = list(data)
    print(f"Keys: {keys}")


def dict_func():
    list_of_tuples = [('APPL', 204), ('IBM', 42), ('MSFT', 32)]
    share_prices = dict(list_of_tuples)
    print(f"Share price: {share_prices}")


def dict_comprehension():
    times_2_table = {x: x * 2 for x in range(10)}
    print(f"Times 2 table: {times_2_table}")


if __name__ == '__main__':
    # dict_demo()
    # dict_func()
    dict_comprehension()
