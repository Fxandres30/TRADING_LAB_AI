class DerivAccount:

    def __init__(self, client):

        self.client = client

    def balance(self):

        return self.client.balance()

    def profile(self):

        return self.client.authorized