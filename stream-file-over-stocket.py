import time
import socket

if __name__ == "__main__":
    filename = input("Enter the file to stream: ")
    host, port = "0.0.0.0", 9999
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((host,port))
    serversocket.listen(1)

    print("Waiting for connection on", host,":", port)
    (client, address) = serversocket.accept()
    print("Connection from", address)
    count = 0
    for line in open(filename):
        print("Row number", count)
        count += 1
        client.send(line)
        time.sleep(0.5)
