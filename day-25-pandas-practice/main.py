import pandas

# data =pandas.read_csv("weather_data.csv")
# print(data)
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# average = data.temp.mean()
# print(average)
# max = data["temp"].max()
# print(max)
#
# print(data.temp)

# # Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
#
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
# temp_f = int(monday.temp) * 1.8 + 32
# print(temp_f)
#
# # Create a DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "Jim", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv", index=False)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(len(data[data["Primary Fur Color"] == "Gray"]))

dict_fur_color = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [0, 0, 0]
}
dict_fur_color["Count"][0] = len(data[data["Primary Fur Color"] == "Gray"])
dict_fur_color["Count"][1] = len(data[data["Primary Fur Color"] == "Cinnamon"])
dict_fur_color["Count"][2] = len(data[data["Primary Fur Color"] == "Black"])

df = pandas.DataFrame(dict_fur_color)
df.to_csv("squirrel_count.csv", index=False)


