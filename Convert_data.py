def get_number_of_line(text):
    number_of_line = ""
    for i in range(13, len(text)):
        if text[i] == ';':
            break
        number_of_line += text[i]
    return number_of_line

def convert(data):
    for line in data:
        #print(f"{line}\n")
        line = line.split(" - ")
        number_of_line = get_number_of_line(line[0])
        print(number_of_line)