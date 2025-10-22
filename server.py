import socket
import subprocess
import os

def start_server():
    # Get host and port from user
    host = input("Enter the host(e.g., 127.0.0.1 or example.com): ")
    port = int(input("Enter the port number (e.g., 8180): "))

    print(f"\n[+] Starting server on {host};{port}...\n")

    try:
        # Create socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Allow reuse of address
        server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
        print("[+]Socket option SO_REUSEADDR enabled.")

        # Bind to host and port
        server_socket.bind((host, port))

        # Start lstening (max 5 queued connections)
        server_socket.listen(5)
        print(f"[+]Server is listening on {host}:{port}")

        # Accept incoming connection
        client_socket, client_address = server_socket.accept()
        print(f"[+]Connection established with {client_address}\n")

        while True:
         try:
            # Receive data from client
            data = client_socket.recv(4096)
            if not data:
                print("[-] Client disconnected.")
                break
                
            command = data.decode('utf-8').strip()
            if command.lower() == "exit":
                print("[+] Client requested disconnection.")
                break

            print(f"[>] Command received: {command}")

            # ---------COMMAND HANDLER --------
            if command startswith("upload"):
                filename = command.split("", 1)[1]
                client_socket.send(b"[READY]")

                # Receive file size
                file_size = int(client_socket.recv(1024).decode())
                client_socket.send(b"[SIZE OK]")

                # Receive file data
                with open(filename, "wb") as f:
                  bytes_read = 0
                  while bytes_read < file_size:
                    chunk = client_socket.recv(4096)
                    if not chunk:
                        break
                    f.write(chunk)
                    bytes_read += len(chunk)
                client_socket.send(f"[+] File '{filename}' uploaded successfully.\n".encode())

              elif command.startswith("download"):
                 filename = command.split("", 1)[1]
                 if os.path.exists(filename):
                    file_size = os.path.getsize(filename)
                    client_socket.send(str(file_size).encode())
                    ack = client_socket.recv(1024)

                    with open(filename, "rb") as f:
                      while chunk := f.read(4096):
                        client_socket.send(chunk)
                    client_socket.send(b"[Done]")
                else:
                  client_socket.send(b"[-]File not found.\n")

              elif command.startswith("view"):
                 filename = command.split("",1)[1]
                 if os.path.exists(filename):
                    with open(filename, "r", encoding="utf-8",errors="ignore")ad f:
                      contents = f.read()
                    client_socket.send(contents.encode())
                else:
                  client_socket.send(b"[-]File not found.\n")

             else:
                # Default: execute system command
                try:
                   result = subprocess.check_output(command,shell=True,stderr=subprocess.STDOUT)
                except subprocess.CalledProcessError as e:
                  result = f"Unexpected error: {e}\n".encode()

                client_socket.send(result)

             except KeyboardInterrupt:
               print("\n[*] Server shutdown requested.")
               break
             except Exception as e:
               print(f"[-] Error:{e}")
               break

          client_socket.close()

       except socket.error as e:
         print(f"Socket error: {e}")
       finally:
          server_socket.close()
          print("[*] Server closed.")

     if_name_ == "_main_":
       start_server()

                        
                    
                                



    
    

    
        
    
                    
        
