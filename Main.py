from Core import Game
from Client import ClientHost
from Server import ServerHost

import sys


def main():
    host = None
    if len(sys.argv) > 1:
        if sys.argv[1] == "client" or sys.argv[1] == "c":
            host = ClientHost()
        elif sys.argv[1] == "server" or sys.argv[1] == "s":
            host = ServerHost()
    else:
        host = ClientHost()
    game = Game(host)


if __name__ == '__main__':
    main()
