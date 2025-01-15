file = open("text1.txt", 'r')
cnt = file.read().split(" ")

if 'sabeeha' in cnt:
    print("Found")
else:
    print("Sorry not found")
