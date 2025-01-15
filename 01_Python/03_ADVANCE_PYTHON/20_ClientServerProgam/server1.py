# SERVER PROGRAM
from socket import *

def main():
    host = gethostname()
    port = 8088

    s = socket()
    s.bind((host, port))
    print("Server is running...")
    s.listen(5)
    c, add = s.accept()
    print(f"Conncetion Established with {c},  {add}")
    msg = c.recv(1024)
    print(msg)
    c.send(b'Hello Client')


main()
