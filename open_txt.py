with open("lines.txt", 'r+') as file:
    pload_list = [line.rstrip('\n') for line in file]
    print(pload_list)
