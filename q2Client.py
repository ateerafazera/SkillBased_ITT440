import socket

def main():
    host = "192.168.75.137"
    port = 8888

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))

        # Receive the quote from the server
        quote = client_socket.recv(1024).decode()

        print("Received Quote of the Day:")
        print(quote)

    except ConnectionRefusedError:
        print("Connection refused. Please ensure the server is running.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    main()
