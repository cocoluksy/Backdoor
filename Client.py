#!/usr/bin/env python3
import socket
import sys

def recv_all(sock, timeout=1.0, bufsize=4096):
    """
    Receive data from `sock` until a short timeout occurs.
    This is useful when the server sends multi-chunk responses and doesn't
    close the connection immediately.
    """
    chunks = []
    sock.settimeout(timeout)
    try:
        while True:
            chunk = sock.recv(bufsize)
            if not chunk:
                break
            chunks.append(chunk)
  
            # If chunk size is smaller than bufsize, likely end of send
            if len(chunk) < bufsize:
                break
    except socket.timeout:
        # no more data arrived within timeout -> return what we have
        pass
    except Exception:
        pass
    finally:
        # Restore blocking mode (no timeout)
        try:
            sock.settimeout(None)
        except Exception:
            pass
    return b"".join(chunks)

def start_client():
    host = input("Enter server host (e.g., 127.0.0.1): ").strip()
    try:
        port = int(input("Enter server port (e.g., 8180): "))
        
    except ValueError:
        print("[-] Invalid port number. Must be an integer.")
        
        return

    try:
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect((host, port))
        print(f"[*] Connected to {host}:{port}")


      
    except Exception as e:
        print(f"[-] Could not connect to {host}:{port} -> {e}")
        return

    try:
        while True:
            try:
                cmd = input("cmd> ").strip()
            except (KeyboardInterrupt, EOFError):
                print("\n[*] Exiting client.")
                break

            if not cmd:
                # send a newline to indicate "no-op" if you want, skip by default
                continue

            # Send the command
            client.sendall(cmd.encode("utf-8"))

            # If user wants to exit
            if cmd.lower() == "exit":
                print("[*] Closing connection as requested...")
                break

            # Receive response (may be multi-chunk)
            response = recv_all(client)
            print("\n--- Server Output ---\n" + response.decode('utf-8', errors='replace') + "\n")
            
    finally:
        try:
            client.close()
        except Exception:
            pass
        print("[*] Client socket closed.")

if __name__ == "__main__":
    start_client()
