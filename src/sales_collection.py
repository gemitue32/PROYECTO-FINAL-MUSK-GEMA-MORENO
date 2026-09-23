class SalesCollection:
    def __init__(self, sales: list):
        self.sales = sales

    # Todas las ventas de un cliente.
    def sales_by_client(self, client_id: int):
        filtered_sales = []
        for sale in self.sales:
            if sale.client_id == client_id:
                filtered_sales.append(sale)
        return filtered_sales

    # Suma de importes de un cliente.
    def total_amount_by_client(self, client_id: int):
        sales = self.sales_by_client(client_id)
        total_amount = 0
        for sale in sales:
            total_amount += sale.amount
        return total_amount   
        
    # Suma de ventas de una categoria.
    def total_amount_by_category(self, category: str):
        total_amount = 0
        for sale in self.sales:
            if sale.category == category:
                total_amount += sale.amount
        return total_amount
    
    #Media de gasto por venta para un cliente.
    def average_sale_by_client(self, client_id: int):
        sales = self.sales_by_client(client_id)
        total_amount = self.total_amount_by_client(client_id)
        if len(sales) == 0:
            return 0
        return total_amount / len(sales)

        