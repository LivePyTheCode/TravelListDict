travel_log = [
    {"Country": "United States",
     "cities_visited": ["Houston", "New York", "Los Angeles", "Miami"],
     "total_visits": 17
     },
    {"Country": "Canada",
     "cities_visited": ["Calagary", "Toronto", "Ottawa"],
     "total_visits": 15
     },

]


def add_new_country(country_visited, cities_visited, times_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["total_visits"] = times_visited
    travel_log.append(new_country)


add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)


def add_new_country2(country_visited, cities_visited, times_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["cities_visited"] = cities_visited
    new_country["total_visits"] = times_visited
    travel_log.append(new_country)


add_new_country2("Mexico", ["Jalisco", "Mexico City"], 2)

print(travel_log)
