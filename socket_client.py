import socket

def client_program():
    host = socket.gethostname()
    port = 7007 #socket server port number

    client_socket = socket.socket() #instantiate
    client_socket.connect((host, port)) #connect to server

    message = input(" -> ") #take input

    while message.lower().strip() != "end":
        clinet_socket.send(message.encode() #send message
        data = cliennt_socket.recv(1024).decode #recieve response

        print('Recieved from server: ' + data)
        message = input(' -> ') #again take input

    client_socket.close() #close connection

if __name__ == '__main__':
    client_program()
