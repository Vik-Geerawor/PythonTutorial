# get the door number
from house.myhouse import DOOR

# get the town name
from pkg.town.mytown import TOWN        # ERROR: does not work

STREET = "Greenwich Way"


if __name__ == "__main__":
    my_address = DOOR + " " + STREET + ", " + TOWN

    print(my_address)
