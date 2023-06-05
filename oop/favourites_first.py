from os import system


class Sorter:
    def __init__(self, favs) -> None:
        self.favs = favs
        self.found = False

    def __call__(self, x):
        if x in self.favs:
            self.found = True
            return (0, x)
        return (1, x)


def main():
    numbers = [8, 3, 1, 2, 9, 5, 4, 7, 6]
    favourites = {7, 3, 8}

    fav_sorter = Sorter(favourites)
    numbers.sort(key=fav_sorter)

    print(numbers)
    print(f"Favourites found: {fav_sorter.found}")


if __name__ == '__main__':
    system('clear')
    main()
