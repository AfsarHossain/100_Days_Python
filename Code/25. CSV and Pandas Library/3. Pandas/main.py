import pandas

data = pandas.read_csv("../weather_data.csv")
# print(data["temp"])
# print(type(data["temp"]))

# TODO: Dictionary
# data_dict = data.to_dict()
# print(data_dict)

# TODO: List
# temp_list = data["temp"].to_list()
# print(len(temp_list))

# TODO: Average
# temp_list = data["temp"].to_list()
# average = sum(temp_list) / len(temp_list)
# print(average)
# print(data["temp"].mean())

# TODO: Maximum
# print(data["temp"].max())

# TODO: Get data in columns
# print(data["condition"])
# print(data.condition)

# TODO: Get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# TODO:
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = int(monday.temp)
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)

# TODO: Create a dataframe from scratch
data_dict = {
    "students": ["Amit", "Jakir", "Afsar"],
    "scores": [75, 58, 65]
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("../data_frame.csv")
