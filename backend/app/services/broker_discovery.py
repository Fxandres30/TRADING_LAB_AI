class BrokerDiscovery:

    def discover(self):

        accounts = []

        accounts.extend(self.discover_mt5())

        accounts.extend(self.discover_deriv())

        return accounts