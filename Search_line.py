def search(lines, start, finish):
    dict = {}
    for line, routes in lines.items():
        for route in routes:
            if start in route and finish in route:
                if route.index(start) < route.index(finish):
                    #print(f"{line} : {route}\n")
                    dict[line] = route
    return dict