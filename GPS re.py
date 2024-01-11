import socket
import pynmea2

def run_client():
    # create a socket object
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_ip = "TYPE YOUR IP"  # replace with the server's IP address
    server_port = 5050  # replace with the server's port number
    # establish connection with server
    client.connect((server_ip, server_port))

    while True:
             # receive message from the server
        response = client.recv(1024)
        response = response.decode("utf-8")
        msg = pynmea2.parse(response)
                
        print("Latitude:",msg.latitude,",","Longitude:",msg.longitude)


run_client()
