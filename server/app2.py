from http.server import HTTPServer
from server import Server
import sys


HOST_NAME = "0.0.0.0"
PORT_NUMBER = 1271

server = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
sys.stderr = open("server/log.txt", "w", 1)


def run():
    server.serve_forever()


if __name__ == "__main__":
    run()