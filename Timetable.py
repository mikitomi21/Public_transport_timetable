from Download_data import get_data
from Convert_data import convert, get_set
from Search_line import search
from Print_informations import print_lines

data = str(get_data())

if not data:
    print("Can't connect with Page")
    exit()


#with open("Timetable_download.txt", "w") as file:
#    file.write(data)

data = data.split("title=")
data = data[3:]
data = convert(data)

#get_set(data)

lines = {}
lines = search(data, "Witosa", "Hallera", 1)
print_lines(lines)
