import http.server
import socketserver
import os
import sys

def main():
    port = 8000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    # root web = current dir PINICOS
    web_root = os.getcwd()
    os.chdir(web_root)

    handler = http.server.SimpleHTTPRequestHandler

    print(f"Serving PINICOS web at http://localhost:{port}")
    print(f"Document root: {web_root}")
    print("CTRL+C to stop\n")

    with socketserver.TCPServer(("", port), handler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped")

if __name__ == "__main__":
    main()
