# with open("weather_data.csv", mode="r") as file:
#     open_file = file.read()

# print(open_file)


import csv 

with open("weather_data.csv") as file_data:                                                                 
    data = csv.reader(file_data)

    temperatures = []

    for row in data:
        if row[1] != 'temp':
            temperatures.append(int(row[1]))

    print(temperatures                                                                                                                                                                                                                                                                  )