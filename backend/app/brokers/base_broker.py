from abc import ABC, abstractmethod


class BaseBroker(ABC):

    def __init__(self, name: str):

        self.name = name
        self.connected = False

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

    @abstractmethod
    def get_balance(self):
        pass

    @abstractmethod
    def get_candles(self):
        pass

    @abstractmethod
    def send_order(self):
        pass