from .Host import Host


class Game:
    def __init__(self, host: Host):
        self.host = host
        self.host.start()
