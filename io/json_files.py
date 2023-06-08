import json


def deserialise_from_json(json_file):
    with open(json_file, 'r', encoding="utf-8") as f:
        x = json.load(f)

    print(type(x))


def serialise_to_json(json_file):
    employee = {"name": "Vik",
                "email": "vik.geerawor@email.com",
                "dob": 15101981}
    print(type(employee))
    with open(json_file, 'w', encoding="utf-8") as f:
        json.dump(employee, f)


if __name__ == '__main__':
    file = 'files/outfile.json'

    # deserialise_from_json(file)
    serialise_to_json(file)
