import socket
import threading
import time

HEADER = 1024
FORMAT = 'utf-8'
DISCONN_MSG = f"QUIT\r\n"
PORT = 45000
IP_ADDR = '0.0.0.0'
ADDR = (IP_ADDR, PORT)

def handle_client(conn, addr):
    print(f"[CONNECTION]: {addr[0]}:{addr[1]} connected")
    connected = True
    
    try:
        while connected:
            msg = conn.recv(HEADER).decode(FORMAT)

            if not msg or DISCONN_MSG in msg:
                connected = False
                continue

            if f"TIME\r\n" in msg:
                curr_time = time.strftime("%H:%M:%S")
                res_msg = f"JAM {curr_time}\r\n"
                conn.send(res_msg.encode(FORMAT))

    except Exception as e:
        print("[ERROR]: ", e)

    finally:
        conn.close()

def start():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING]: server is listening")

    try:
        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS]: {threading.active_count() - 1}")

    except KeyboardInterrupt:
        print("[CLOSING]: server is closing")

    finally:
        server.close()

if __name__ == "__main__":
    start()
