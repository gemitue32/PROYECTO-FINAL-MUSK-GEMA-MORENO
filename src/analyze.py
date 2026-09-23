import json
import csv
from client import Client
from client_collection import ClientCollection
from sale import Sale
from sales_collection import SalesCollection

# Leer clients.json
with open("data/clients.json", "r") as archivo:
    clients_data = json.load(archivo)

# Convertir cada diccionario en un objeto Client
clients = []

for client_data in clients_data:
    new_client = Client(
        client_data["client_id"],
        client_data["name"],
        client_data["country"],
        client_data["signup_date"]

        )
    clients.append(new_client)

# Crear la colección
clients_collection = ClientCollection(clients)

# Leer sales.csv
with open("data/sales.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    sales_data = list(lector)

# Convertir cada diccionario en un objeto Sale
sales = []
for sale_data in sales_data:
    new_sale = Sale(
        int(sale_data["sale_id"]),
        int(sale_data["client_id"]),
        sale_data["product"],
        sale_data["category"],
        float(sale_data["amount"]),
        sale_data["date"]
        )
    sales.append(new_sale)

# Crear la colección
sales_collection = SalesCollection(sales)

#--Ejercicios--

# 1. Número total de clientes.

total_clients = len(clients)

# 2. Número total de ventas.

total_sales = len(sales)

# 3. Total de ingresos por clientes.

clients_info = []
for client in clients:
    total_spent = sales_collection.total_amount_by_client(client.client_id)
    sale_count = len(sales_collection.sales_by_client(client.client_id))
    average_sale = sales_collection.average_sale_by_client(client.client_id) 
    client_summary = {
        "client_id": client.client_id,
        "name": client.name,
        "total_spent": total_spent,
        "sale_count": sale_count,
        "average_sale": average_sale
    }
    


 


