# # with open("weather_data.csv") as file:
# #     data = file.readlines()
# # print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as file:
# #     data = csv.reader(file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(data["temp"])
# # print(data.to_dict())
# #
# # temp_list = data["temp"].to_list()
# # print(temp_list)
# #
# # avg_temp = sum(temp_list)/len(temp_list)
# # print(avg_temp)
# # print(data["temp"].mean())
# #
# # print(f"Max temperature is: {data["temp"].max()}")
# # print(data.day)
#
# # print(data[data.day == "Monday"])
# # print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day == "Monday"]
# # # print(monday.condition)
# # print(monday.temp[0]*9/5+32)
#
# data_dict = {
#     "students" : ["Taku", "Papy", "Koko"],
#     "scores" : [60, 80, 70],
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
#

import pandas

squirrels = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240827.csv")
squirrel_colors = squirrels["Primary Fur Color"]
# squirrel_count = squirrel_colors.value_counts()
# squirrel_count.to_csv("squirrel_count.csv")
grey_count = 0
red_count = 0
black_count = 0
for color in squirrel_colors:
    if color == "Gray":
        grey_count += 1
    elif color == "Cinnamon":
        red_count += 1
    elif color == "Black":
        black_count += 1

# print(f"Gray: {grey_count}, Red: {red_count}, Black: {black_count}")

squirrel_color_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_count, red_count, black_count]
}

df = pandas.DataFrame(squirrel_color_dict)
df.to_csv("squirrel_count.csv")