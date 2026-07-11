from app.core.service import Service


class RiskManager(Service):

    def __init__(self, event_bus):

        super().__init__()

        self.event_bus = event_bus