class EmailService:
    def update(self, order_id):
        print(f'Sending email confirmation: {order_id}')

class InventorSystem():
    def update(self, order_id):
        print(f'Updating stock list for {order_id}')

class SMSNotifier:
    def update(self, order_id):
        print(f'texting about order{order_id}')

class Order:
    def __init__(self, order):
        self.order_id = self.order_id
        self.clients = []

    def add_client(self, c):
        self.clients.append(c)

    def notify(self):
        for c in self.clients:
            c.update(self.order_id)

    def ship(self):
        print(f'Order {self.order_id} Shipped')
        self.notfiy()