import socket

def main():
    connect_ip = "192.168.1.113"
    connect_port = 9999
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect( (connect_ip, connect_port) )
    print sock.recv(1024)
    
    while True: 
        data = raw_input("Client0: ")
        sock.send(data)
        if data == "exit":
            break
        print "Server: %s" % sock.recv(1024)

    s.close()
    
if __name__ == "__main__":
    main()
