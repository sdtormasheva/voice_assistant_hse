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
    locations = get_locations()
    if name not in locations:
        locations[name] = point
        update_locations(locations)
        return "ok"
    else:
        return "already exists"


def remove_location(name):
    locations = get_locations()
    if name in locations:
        locations.pop(name, None)
        update_locations(locations)
        return "ok"
    else:
        return "not found"


def get_by_name(name):
    locations = get_locations()
    if name in locations:
        return locations[name]
    else:
        return "not found"
