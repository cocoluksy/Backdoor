import socket
import sys
import subprocess

def start_server():
    """Start a simple TCP command server (for controlled local testing)."""
    
    host = input("Enter the host (e.g., 127.0.0.1 or localhost): ").strip()
    port_input = input("Enter the port number (e.g., 8180): ").strip()

    # Validate port
    try:
        port = int(port_input)
        if not (1 <= port <= 65535):
            print("Invalid port number. Must be between 1 and 65535.")
            return
    except ValueError:
        print("Invalid port number.")
        return

    # Create socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        # Bind and listen
        server_socket.bind((host, port))
        server_socket.listen(5)
        print(f"[+] Server started, listening on {host}:{port}")

        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"[+] Connection established with {client_address}")

        with client_socket:
            while True:
                data = client_socket.recv(1024)
                if not data:
                    print("[-] Client disconnected.")
                    break

                command = data.decode('utf-8').strip()
                print(f"[>] Received command: {command}")

                if command.lower() == "exit":
                    print("[*] Client requested disconnection.")
                    client_socket.send(b"Goodbye!\n")
                    break

                # Controlled command execution
                try:
                    # Execute only safe commands (example: 'dir' or 'ls')
                    if command.lower() in ['ls', 'dir', 'whoami', 'pwd']:
                        result = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
                    else:
                        result = b"Command not allowed.\n"
                except subprocess.CalledProcessError as e:
                    result = e.output or b"Error executing command.\n"

                client_socket.send(result)

    except socket.error as e:
        print(f"[-] Socket error: {e}")
    except KeyboardInterrupt:
        print("\n[*] Server shutdown requested.")
    finally:
        server_socket.close()
        print("[*] Server socket closed.")


if __name__ == "__main__":
    start_server()
