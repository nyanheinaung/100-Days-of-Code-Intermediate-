try:
    testDict = {"key": "value"}
    print(testDict["key1"])
    file = open("file.txt", "r")
    print(file)
except FileNotFoundError:
    file = open("file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"key {error_message} does not exist")
else:
    content = file.read()
    print(content)
# finally:
#     raise TypeError("This is a made up error")

