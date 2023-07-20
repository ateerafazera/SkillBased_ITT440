#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <arpa/inet.h>

#define PORT 8686

int main() {
    int sock = 0, valread;
    struct sockaddr_in serv_addr;
    int random_number;

    // Create a TCP socket
    if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("socket failed");
        exit(EXIT_FAILURE);
    }

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(PORT);

    // Convert IPv4 and IPv6 addresses from text to binary form
    if (inet_pton(AF_INET, "192.168.75.137", &serv_addr.sin_addr) <= 0) {
        perror("Invalid address/ Address not supported");
        exit(EXIT_FAILURE);
    }

    // Connect to the server
    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)>
        perror("Connection failed");
        exit(EXIT_FAILURE);
    }

    // Receive the random number from the server
    valread = recv(sock, &random_number, sizeof(random_number), 0);

    if (valread > 0) {
        printf("Received random number from the server: %d\n", random_number>
    } else {
        printf("Failed to receive random number from the server.\n");
    }

    close(sock);
    return 0;
}
