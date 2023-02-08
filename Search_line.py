"""
parameter flag
    0->The function will return the whole list of streets
    1->The function will return the list of streets that have to travel by to reach a goal
"""
def search(lines, start, finish, flag=0):
    dict = {}

    for line, routes in lines.items():
        for route in routes:
            if start in route and finish in route:
                if route.index(start) < route.index(finish):
                    #print(f"{line} : {route}\n")
                    if flag == 0:
                        dict[line] = route
                    elif flag == 1:
                        dict[line] = route[route.index(start):route.index(finish)+1]
                    else:
                        return dict

    return dict