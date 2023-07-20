import socket

def main():
    host = "izani.synology.me"
    port = 8443

    try:
        # Create a socket object
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set a timeout for the connection (optional)
        client_socket.settimeout(10)

        # Connect to the server
        client_socket.connect((host, port))

        print(f"Successfully connected to {host} on port {port}")

        # Get user input for the message
        message = input("Enter your message: ")

        # Send the user input message to the server
        client_socket.send(message.encode())

        # Receive response from the server
        response = client_socket.recv(4096).decode()
        print("Server response:", response)

        # Close the socket when done
        client_socket.close()

    except socket.error as e:
        print(f"Error connecting to {host} on port {port}: {e}")
        # Handle the error appropriately

if __name__ == "__main__":
    main()
