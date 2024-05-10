import socket

IP_ADDR = '172.18.0.3'
PORT = 45000
ADDR = (IP_ADDR, PORT)
FORMAT = 'utf-8'

def get_time(client_socket):
    request = f"TIME\r\n"
    client_socket.send(request.encode(FORMAT))

    response = b""
    data = client_socket.recv(1024)
    response += data

    print(response.decode(FORMAT).strip())

def connect():
    try:
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect(ADDR)

        while True:
            option = int(input("Enter selection: "))
            if option == 1:
                get_time(client_socket)
            elif option == 2:
                print("Quitting...")
                break
            else:
                print("Please enter a valid option!")

    except Exception as e:
        print("Error:", e)

    finally:
        client_socket.close()

def start():
    print('''
Please press:
1. To get current time
2. To quit connection
    ''')
    connect()        

if __name__ == "__main__":
    start()
