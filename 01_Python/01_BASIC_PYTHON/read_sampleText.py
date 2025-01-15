file = open("text1.txt", 'r')
cnt = file.read().split(" ")

if 'Sabeeha' in cnt:
    print("Found")
else:
    print("Sorry not found")
