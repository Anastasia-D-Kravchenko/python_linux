from threading import Thread
import socket

def check_port(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")
    sock.close()

def main():
    host = 'pja.edu.pl'
    ports = [80, 22, 443, 21]

    threads = []
    for port in ports:
        thread = Thread(target=check_port, args=(host, port,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == '__main__':
    main()