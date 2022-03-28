with open("data.txt") as file:
    content = file.read()
    num = int(content)
    print(num, type(num))