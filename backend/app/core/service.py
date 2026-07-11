from abc import ABC


class Service(ABC):

    def __init__(self):

        self.running = False

    def start(self):

        if self.running:
            return

        self.running = True

        print(f"✅ {self.__class__.__name__} iniciado")

    def stop(self):

        if not self.running:
            return

        self.running = False

        print(f"🛑 {self.__class__.__name__} detenido")

    def status(self):

        return {
            "service": self.__class__.__name__,
            "running": self.running
        }