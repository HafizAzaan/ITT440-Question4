import socket
import threading
import random

# List of quotes
quotes = [
    "Be yourself; everyone else is already taken. - Oscar Wilde",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
    "In the end, it's not the years in your life that count. It's the life in your years. - Abraham Lincoln",
    "Life is what happens when you're busy making other plans. - John Lennon",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill"
]

def handle_client(client_socket):
    quote = random.choice(quotes)
    client_socket.send(quote.encode('utf-8'))
    client_socket.close()

def start_server():
    server_ip = "127.0.0.1"
    server_port = 8888

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f"[*] Quote of the Day server is listening on {server_ip}:{server_port}")

    while True:
        client_socket, client_addr = server_socket.accept()
        print(f"[*] Accepted connection from {client_addr[0]}:{client_addr[1]}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
