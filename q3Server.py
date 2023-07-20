import socket
import os

def convert_to_atm(pressure_bar):
    # Conversion from bar to atm
    return pressure_bar * 0.986923

def handle_client(client_socket):
    try:
        # Receive pressure value in bar from the client
        pressure_bar = float(client_socket.recv(1024).decode())

        # Convert pressure to atmosphere-standard (atm)
        pressure_atm = convert_to_atm(pressure_bar)

        # Send the converted pressure value back to the client
        client_socket.send(str(pressure_atm).encode())

    except Exception as e:
        print("Error:", e)

    finally:
        # Close the client socket
        client_socket.close()

def main():
    host = "192.168.75.137"
    port = 8686

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen()

    print("Server is listening on port", port)

    while True:
        # Accept a new connection from the client
        client_socket, client_address = server_socket.accept()
        print("Connected to:", client_address)

        # Fork a new process to handle the client connection
        pid = os.fork()

        if pid == 0:
            # This is the child process
            # Close the server socket in the child process
            server_socket.close()

            # Handle the client connection
            handle_client(client_socket)

            # Exit the child process
            os._exit(0)

        else:
            # This is the parent process
            # Close the client socket in the parent process
            client_socket.close()

if __name__ == "__main__":
    main()
