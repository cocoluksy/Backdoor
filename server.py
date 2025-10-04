import socket
import sys

def start_server():
    # Get host and port from user
    


    # Intructions to Display connection information
    

    try:
        # Create socket
        
        
        # Allow reuse of address
        
        
        # Bind to host and port
        
        
        # Start listening (max 5 queued connections)
        

        # Accept incoming connection
        

        # Receiving commands loop
        while True:
            try:
                # Receive data from client
                
                
                # You can add command processing logic here
                # For example, execute commands and send back results
                
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
       

if __name__ == "__main__":
    start_server()