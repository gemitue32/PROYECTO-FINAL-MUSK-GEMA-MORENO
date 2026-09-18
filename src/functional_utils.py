from datetime import datetime
from functools import reduce

def filter_sales_by_category(sales, category):
    return list(filter(lambda s: s.category == category, sales))

def filter_sales_by_date_range(sales, start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return list(filter(lambda s: datetime.strptime(s.date, "%Y-%m-%d") >= start and datetime.strptime(s.date, "%Y-%m-%d") <= end, sales))

def map_sale_amounts(sales):
    return list(map(lambda s: s.amount, sales))

def reduce_total_amount(sales):
    return reduce(lambda acumulado, s: acumulado + s.amount, sales, 0)

def filter_clients_by_min_spent(clients, sales_collection, minimum):
    return list(filter(lambda c: sales_collection.total_amount_by_client(c.client_id) > minimum, clients))
    
    