import time
word = "test"
x = word * 1000000000
time.sleep(10)
print("This message wont appear if stack overflow has occurred!")
