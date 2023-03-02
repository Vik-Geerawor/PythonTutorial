def lists():
    shopping_list = ['banana', 'apple', 'coconut', 'mango', 'strawberry']
    print(f'Item 1: {shopping_list[0]}')
    print(f'Last item: {shopping_list[-1]}')

    favourites = shopping_list[0:3]
    print(f'My favourties: {favourites}')
    print(f'My favourties in reverse: {favourites[::-1]}')
    favourites.append(shopping_list[-2])
    print(f'My new favourties: {favourites}')


def main():
    lists()
