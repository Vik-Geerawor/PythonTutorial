def if_condition():
    x = int(input('Enter an grade: '))
    if x < 50:
        print(f'Fail')
    elif 60 > x >= 50:
        print(f'Pass')
    elif 70 > x >= 60:
        print(f'Merit')
    elif x >= 70:
        print(f'Distinct')
    else:
        print(f'Error')


def match_demo(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"


def http_error_types(code):
    match code:
        case code if 100 <= code < 200:
            return 'Informational responses'
        case code if 200 <= code < 300:
            return 'Successful responses'
        case code if 300 <= code < 400:
            return 'Redirection messages'
        case code if 400 <= code < 500:
            # TODO: function call
            return str(code) + ' - ' + 'Client error responses' + ' - ' + http_client_error(code)
        case code if 500 <= code < 600:
            return 'Server error responses'


def http_client_error(code):
    match code:
        case 400:
            return 'Bad Request'
        case 401:
            return 'Unauthorised'
        case 402:
            return 'Payment Required'
        case 403:
            return 'Forbidden'
        case 404:
            return 'Not Found'
        case 405:
            return 'Method Not Allowed'
        case _:
            return 'Unknown Error'


def advanced_conditions():
    """
    'in' and 'not in' - membership test
    'is' and 'is not' - checks if 2 objects are really the same object
    """

    fridge = ['apple', 'mango', 'strawberry']
    shopping_list = ['banana', 'apple', 'coconut']

    print(f"Fridge: {fridge}")
    print(f"shopping list: {shopping_list}")

    for item in fridge:
        if not item in shopping_list:
            shopping_list.append(item)

    print(f"Fridge: {fridge}")
    print(f"shopping list (updated): {shopping_list}")


if __name__ == '__main__':
    # if_condition()
    # print(http_error(400))
    # print(http_error_types(404))
    advanced_conditions()
