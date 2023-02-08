from Download_data import get_data
from Convert_data import convert

data = str(get_data())

if not data:
    print("Can't connect with Page")
    exit()


#with open("Timetable_download.txt", "w") as file:
#    file.write(data)

data = data.split("title=")
data = data[3:]

data = convert(data)

for line, routes in data.items():
    for route in routes:
        print(f"{line} : {route}\n")