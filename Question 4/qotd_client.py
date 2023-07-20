import socket

def get_quote_from_server():
    server_ip = "127.0.0.1"
    server_port = 8888

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_ip, server_port))

    quote = client_socket.recv(1024).decode('utf-8')
    print(f"Quote of the day: {quote}")

if __name__ == "__main__":
    get_quote_from_server()
