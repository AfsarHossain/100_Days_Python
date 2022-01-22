try:
    file = open("data.txt")
    dictionary = {"key": "value"}
    print(dictionary["key"])
except FileNotFoundError:
    # print("There was an error")
    file = open("data.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"That key {error_message} does not exists.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File was closed.")
    # raise TypeError("This is an error that I made up.")
