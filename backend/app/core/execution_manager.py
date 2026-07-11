from app.core.service import Service


class ExecutionManager(Service):

    def __init__(self, event_bus):

        super().__init__()

        self.event_bus = event_bus

    # =====================================
    # ORDENES
    # =====================================

    def buy(self, broker, order):

        return broker.send_order(order)

    def sell(self, broker, order):

        return broker.send_order(order)

    def close(self, broker, position):

        return broker.positions.close(position)