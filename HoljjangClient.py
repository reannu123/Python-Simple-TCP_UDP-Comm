import socket

def main():

    # Initialize TCP connection
    clientsocket = socket.socket(
        socket.AF_INET,
        socket.SOCK_STREAM)
    
    # Connect to server with designated IP address and port number
    clientsocket.connect((
        "10.0.2.6", 
        58913)) 

    # Initialize UDP connection
    serverSock = socket.socket(
        socket.AF_INET,
        socket.SOCK_DGRAM)
    # Bind socket to local host and port
    serverSock.bind(('',6789))


    game = True             # Game loop variable (if the game is still running)

    # Game loop
    while(game):
        s = input()

        # Send message s to the server
        clientsocket.send(s.encode())

        message = ""        # Temporary string to hold message to be received from server

        # Loop until a message is received from the server
        while True:
            data, addr = serverSock.recvfrom(1024)  # Receive message from server
            if len(data) > 0:                       # If message is not empty
                message = data.decode()                 # Decode message
                break                                   # Break out of loop

        
        print(message)                              # Print message received from server
        if message == "Goodbye!":                   # If message is "Goodbye!", end game
            game = False                    # Set game to False to end game loop
            clientsocket.close()            # Close TCP connection
            break                           # Break out of game loop
        
# If this file is run as a script, run main()
if __name__ == "__main__":
    main()