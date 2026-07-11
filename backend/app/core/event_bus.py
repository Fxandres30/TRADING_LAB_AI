from collections import defaultdict


class EventBus:

    def __init__(self):

        self.events = defaultdict(list)

    def subscribe(self, event_name, callback):

        self.events[event_name].append(callback)

    def publish(self, event_name, data=None):

        if event_name not in self.events:
            return

        for callback in self.events[event_name]:
            callback(data)