import socket
import sys

def start_server():
    # Get host and port from user
    host = input("Enter the host (e.g., 127.0.0.1 or example.com): ")
    port = int(input("Enter the port number (e.g 8180): "))


    # Intructions to Display connection information
    


    try:
        # Create socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        
        
        # Allow reuse of address
        server_socket.setsockopt(socket.send.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print("Socket option SO_REUSEADDR is now enabled.")
        
        
        # Bind to host and port
        server_socket.bind((host, port))
        
        # Start listening (max 5 queued connections)
        server_socket.listen(5)
        print(f"Server listening on {host}:{port}")

        # Accept incoming connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")
        
        

        # Receiving commands loop
        while True:
            try:
                # Receive data from client
                data = client_socket.recv(1024)
                
                
                # You can add command processing logic here
                command = data.decode('utf-8').strip()
                if not command:
                    break
                if command.lower() == "exit":
                    print("Client requested disconnection")
                # For example, execute commands and send back results
                try:
                    result = subprocess.check_output(command, shell=True, stderr=subproces.STDOUT)
                except subprocess.CalledprocessError as e:
                    result = e.output or b"Error executing command.\n"
                client_socket.send(result)
                
                # Echo back to client (replace this with your command processing)
                response = f"Server received: {data}"
                client_socket.send(response.encode('utf-8'))
                
            except KeyboardInterrupt:
                print("\n[*] Server shutdown requested")
                break
            except Exception as e:
                print(f"[-] Error: {e}")
                break

    except socket.error as e:
        print(f"Socket error: {e}")
       

if __name__ == "__main__":
    start_server()