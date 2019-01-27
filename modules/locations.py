import json


locations_file = 'test.json'


def get_locations():
    with open(locations_file) as f:
        locations = json.load(f)
    return locations


def update_locations(locations):
    with open(locations_file, 'w') as f:
        json.dump(locations, f)


def add_location(name, point):
    name_clear = name.lower()
    locations = get_locations()
    if name_clear not in locations:
        locations[name_clear] = point
        update_locations(locations)
        return "ok"
    else:
        return "already exists"


def remove_location(name):
    name_clear = name.lower()
    locations = get_locations()
    if name_clear in locations:
        locations.pop(name_clear, None)
        update_locations(locations)
        return "ok"
    else:
        return "not found"


def get_by_name(name):
    name_clear = name.lower()
    locations = get_locations()
    for key in locations:
        if name_clear == key:
            return locations[key]
    return "not found"
