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
    last_route = text[len(text)-1]
    street = ""
    for i in range(len(last_route)):
        if last_route[i]=='"':
            break
        street += last_route[i]
    text[len(text) - 1] = street

    return text


def divide_list_on_two(route):
    routes = route.split("\\r\\n\\r\\")
    print(routes)


def add_routes_to_dictionary(dict, line, routes):
    #todo add to dictionary key[number_of_line]->value[route]
    #todo route is a string, change it to list and use divide_list_on_two funtion to divide it and save into dictionary
    pass


def convert(data):
    lines = {}
    for line in data:
        #print(f"{line}\n")

        line = line.split(" - ")
        number_of_line = get_number_of_line(line[0])
        #print(number_of_line)
        route_of_line = get_route_of_line(line)
        add_routes_to_dictionary(lines, number_of_line, route_of_line)
        #lines[number_of_line] =