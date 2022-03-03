import socket
import threading

def tcpsock(sock, addr):
    print "Accepted new connection from %s:%d" % (addr[0], addr[1])
    sock.send('If you want to interrupt the chatting, enter the "exit"')
    while True:
        data = sock.recv(1024)
        if data == "exit":
            break
        print "Client: %s" % data
        data = raw_input("Server: ")
        sock.send(data)
    sock.close()
    print "Connection from %s:%s has be closed" % (addr[0], addr[1])

def main():
    bind_ip = "0.0.0.0"
    bind_port = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind( (bind_ip, bind_port) )
    s.listen(5) 
    print "Listening on %s:%d" % (bind_ip, bind_port)

    while True:
        sock, addr = s.accept()
        t = threading.Thread( target=tcpsock, args=(sock, addr) )
        t.start()

if __name__ == "__main__":
    main()
