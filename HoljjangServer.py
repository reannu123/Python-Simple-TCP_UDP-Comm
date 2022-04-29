import socket
import random

# TCP Server
def main():

    # Initialize TCP connection
    serversocket = socket.socket(
        socket.AF_INET, 
        socket.SOCK_STREAM)
        
    # Bind socket to local host and port
    serversocket.bind(('',58913))

    # Listen for incoming connections
    serversocket.listen(5)

    # Accept incoming connections
    connection,address = serversocket.accept()

    # Initialize UDP connection
    clientSock = socket.socket(
        socket.AF_INET, 
        socket.SOCK_DGRAM)
    

    s = ""          # Temporary string to hold message received from client
    c_score = 0     # Client's score
    s_score = 0     # Server's score
    game = True     # Game loop variable (if the game is still running)
    winner = ""     # Temporary string to hold winner
    notif = ""      # Temporary string to hold message to be sent to client

    # Game loop
    while (game):


        # Receive message from client
        s = tcp_receive(connection)



        # If the client sends "exit", end the game
        if s == "exit":
            game = False        # Set game to False to end game loop

            # Send "Goodbye!" message to client
            udp_send(clientSock, "Goodbye!")

            # Close TCP connection
            serversocket.close()

            # break out of game loop
            break              


        # Roll a random number between 1 and 10 and store to num
        num = random.randint(1, 10)

        s_comp = ""             # Temporary string to hold num's category
        
        if num%2 == 0:      
            s_comp = "even"     # If the random number is even, set s_comp to even
        
        else:
            s_comp = "odd"      # If the random number is odd, set s_comp to odd



        if s == s_comp:         # If the client and server's random number are the same
            winner = "CLIENT WINS!\n"       # Set winner to client
            c_score += 1                    # Increment client's score
        
        else:                   # If the client and server's random number are different
            winner = "SERVER WINS!\n"       # Set winner to server
            s_score += 1                    # Increment server's score


        # Create score string
        score = "Client: " + str(c_score) + ", Server: " + str(s_score)     

        # Create notification string
        notif = winner + score                         

        # Print notification string on server console                    
        print(notif)    

        # Send notification string to client
        udp_send(clientSock, notif)


# Function for receiving TCP messages
def tcp_receive(connection):
    s = ""  # Temporary string to hold message received from client

    # Loop until a message is received from client
    while True:
        buf = connection.recv(64)       # Receive message from client
        if len(buf) > 0:                # If message is not empty
            s = buf.decode()                # Decode message from bytes to string
            break                           # Break out of loop

    return s                # Return message received from client


# Function for sending UDP messages
def udp_send(clientSock, message):

    UDP_IP_ADDRESS = "10.0.2.5"         # IP address of the client we are sending to
    UDP_PORT_NO = 6789                  # Port number of the client we are sending to

    Message = message.encode()          # Encode message to bytes

    
    clientSock.sendto(                  # Send message to host
        Message, 
        (UDP_IP_ADDRESS,UDP_PORT_NO))


# If this file is run as a script, run main()
if __name__ == "__main__":              
    main()                              