import json

data = {}


def add_counting(author, system):
    try:
        data["counting"]["total"][author] += 1
    except KeyError:
        data["counting"]["total"][author] = 1
    
    try:
        data["counting"][system][author] += 1
    except KeyError:
        data["counting"][system][author] = 1


def load_data():
    with open("data.json") as data_file:
        raw_data = data_file.read()
    data = json.loads(raw_data)
    return(data)


def save_data(data):
    raw_data = json.dumps(data, indent=4)
    with open("data.json", "w") as data_file:
        data_file.write(raw_data)