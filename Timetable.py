from Download_data import get_data

data = str(get_data())

if not data:
    print("Can't connect with Page")
    exit()


#with open("Timetable_download.txt", "w") as file:
#    file.write(data)

data = data.split("title=")
data = data[3:]
print(data)