import socket
import threading
import random

# List of quotes
quotes = [
    "The best among you is the one who doesn’t harm others with his tongue and hands. - Prophet Muhammad",
    "Never trust anything that can think for itself if you can't see where it keeps its brain. - J. K. Rowling",
    "I leave behind me two things, The Quran and My Sunnah and if you follow these you will never go astray. - Prophet Muhammad",
    "When in doubt, don't. - Benjamin Franklin",
    "Love has no errors, for all errors are the want for love. - William Law",
    "Be yourself; everyone else is already taken. - Oscar Wilde",
    "The other night I ate at a real nice family restaurant. Every table had an argument going. - George Carlin",
    "Worldly life is short, so turn to Allah before you return to Allah. – Anonymous",
    "The only thing we have to fear is fear itself. - Franklin D. Roosevelt",
    "You are never too old to set another goal or to dream a new dream. - C.S. Lewis"
]

def handle_client(client_socket):
    # Get a random quote
    random_quote = random.choice(quotes)

    # Send the quote to the client
    client_socket.send(random_quote.encode())

    # Close the client socket
    client_socket.close()

def main():
    host = "192.168.75.137"
    port = 8888

    # Create a TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen()

    print("QOTD server is listening on port", port)

    while True:
        # Accept a new connection from the client
        client_socket, client_address = server_socket.accept()

        print("Connected to:", client_address)

        # Create a new thread to handle the client connection
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    main()
