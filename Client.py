#!/usr/bin/env python3
import socket
import sys

def recv_all(sock, timeout=1.0, bufsize=4096):
    """
    Receive data from `sock` until a short timeout occurs.
    This is useful when the server sends multi-chunk responses and doesn't
    close the connection immediately.
    """

  
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
        
    except ValueError:
        
        return

    try:


      
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
            

            # If user wants to exit
            

            # Receive response (may be multi-chunk)
            
    finally:
        try:
            client.close()
        except Exception:
            pass
        print("[*] Client socket closed.")

if __name__ == "__main__":
    start_client()
