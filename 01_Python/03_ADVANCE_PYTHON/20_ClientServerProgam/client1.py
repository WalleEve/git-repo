# CLIENT PROGRAM
from socket import *

def main():
    host = gethostname()
    port = 8088

    s = socket()

    s.connect((host, port))

    s.send(b'Hello Server')

    msg = s.recv(1024)
    print(msg)

    s.close()

main()
