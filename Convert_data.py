def get_number_of_line(text):
    number_of_line = ""
    for i in range(13, len(text)):
        if text[i] == ';':
            break
        number_of_line += text[i]
    return number_of_line


def get_route_of_line(text):
    # change the first element of list
    first_route = text[0]
    first_route = first_route.split(": ")
    street = first_route[1]
    text[0] = street

    # change the last element of list
    last_route = text[len(text) - 1]
    street = ""
    for i in range(len(last_route)):
        if last_route[i] == '"':
            break
        street += last_route[i]
    text[len(text) - 1] = street

    return text


def divide_list_on_two(route):
    number_of_street = 0

    while not '\r' in route[number_of_street]:
        number_of_street += 1
        # Situation that the route doesn't represent a route of line, but some extra information
        if number_of_street == len(route):
            return False, False

    end_route = route[number_of_street]

    for i in range(len(end_route)):
        if not end_route[i] == '\r':
            continue
        route[number_of_street] = end_route[:i]
        # Duplicate last street
        route.insert(number_of_street, end_route[:i])
        break

    # return first and second route of this line
    number_of_street += 1
    first_route = route[:number_of_street]
    second_route = route[number_of_street:]

    return first_route, second_route


def add_routes_to_dictionary(dict, line, routes):
    first_route, second_route = divide_list_on_two(routes)
    if not first_route:
        return dict
    list_of_routes = [first_route, second_route]
    dict[line] = list_of_routes
    return dict


def convert(data):
    lines = {}
    for line in data:
        # print(f"{line}\n")
        line = line.split(" - ")
        number_of_line = get_number_of_line(line[0])
        # print(number_of_line)
        route_of_line = get_route_of_line(line)

        lines = add_routes_to_dictionary(lines, number_of_line, route_of_line)

    return lines

def get_set(data):
    set_of_streets = set()
    for line in data:
        for route in data[line]:
            #print(route)
            for street in range(len(route)):
                set_of_streets.add(route[street])
    print(set_of_streets)