import socket

def server_program():
    host = socket.gethostname() #localhost
    port = 7007 

    server_socket = socket.socket() #get instance
    server_socket.bind((host, port)) #bind host address and port together

    server_socket.listen(1) #server can listen to 1 client
    conn, address = server_socket.accept() #accept new connection

    while True:
        data = conn.recv(1024).decode()#recieve data stream max data packet 1024 bytes
        if not data:
            #if data is not recieved
            break
        print("From client: " + str(data))
        data = inpit(' -> ')
        conn.send(data.encode()) #send data to client

    conn.close() #close connection

if __name__ == '__main__':
    server_program()
