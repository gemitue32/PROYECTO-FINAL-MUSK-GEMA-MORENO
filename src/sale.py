class Sale:
    # sale_id es texto en el CSV real (S1001, S1002...), aunque el PDF indicaba int
    def __init__(self, sale_id: str, client_id: int, product: str, category: str, amount: float, date: str):
        self.sale_id = sale_id
        self.client_id = client_id
        self.product = product
        self.category = category
        self.amount = amount
        self.date = date

    # Convierte el objeto a un diccionario Python para poder exportarlo como JSON.
    def to_dict(self):
        return {
            "sale_id": self.sale_id,
            "client_id": self.client_id,
            "product": self.product,
            "category": self.category,
            "amount": self.amount,
            "date": self.date
        }
