# SERVER PROGRAM AAP

# import required module

import os
import socket
import time

def create_socket():
    global host
    global port
    global sokt

    try:
        host = socket.gethostname()
        port = 9090
        sokt = socker.socket()
    except socket.error as msg:
        print(f"Socket Creation Error: {msg}")


def bind_socket():
    global host
    global port
    global sokt

    try:
        print(f"Bindind the port: {port}")
        sokt.bind((host, port))

        # number of client can connect
        sokt.listen(5)
    except socket.error as msg:
        print(f"Socket Binding Error {msg}", end='\n')
		print("Retying...")
		bind_socket()


def socet_accept():
	conn, add = s.accept()
	print(f"Conncetion Established with {add}")

	send_command(conn)		
	conn.close()
