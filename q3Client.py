
import socket

def main():
    host = "192.168.75.137"
    port = 8686

    # Create a TCP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    # Get user input for pressure value in bar
    pressure_bar = float(input("Enter pressure value in bar: "))

    # Send the pressure value to the server
    client_socket.send(str(pressure_bar).encode())

    # Receive the converted pressure value from the server
    pressure_atm = float(client_socket.recv(1024).decode())

    # Display the received atmosphere-standard value
    print(f"Pressure in atmosphere-standard (atm): {pressure_atm:.4f} atm")

    # Close the socket
    client_socket.close()

if __name__ == "__main__":
    main()
