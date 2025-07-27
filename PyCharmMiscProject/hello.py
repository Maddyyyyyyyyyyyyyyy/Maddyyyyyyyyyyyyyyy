with open("ding.txt","r") as file:
    lines = file.readline()
    for line in file[1:]:
        maadesh = line.strip().split(",")
        print(maadesh(2))

