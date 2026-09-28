import json
import csv
import pandas as pd
from src.client import Client
from src.client_collection import ClientCollection
from src.sale import Sale
from src.sales_collection import SalesCollection
from src.functional_utils import filter_sales_by_category, reduce_total_amount

def generate_report():
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
            (sale_data["sale_id"]),
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

    # Cálculo 3, 4 y 5: total gastado, número de ventas y promedio por venta de cada cliente
    # (se calculan juntos porque los tres acaban en el mismo diccionario del JSON final)

    clients_info = []
    for client in clients:
        total_spent = sales_collection.total_amount_by_client(client.client_id)
        sale_count = len(sales_collection.sales_by_client(client.client_id))
        average_sale = round(sales_collection.average_sale_by_client(client.client_id), 2)
        client_summary = {
            "client_id": client.client_id,
            "name": client.name,
            "total_spent": total_spent,
            "sale_count": sale_count,
            "average_sale": average_sale
        }
        clients_info.append(client_summary)        

    # 6. Cliente con mayor gasto por país. 
    # Agrupar clientes por country (POO)
    # Calcular gastos por cliente (colección de ventas)
    # Elegir el de mayor total                
        
    clients_country = set(map(lambda x: x.country, clients))
    top_client_by_country = {}
    for country in clients_country:
        clients_of_country = clients_collection.clients_by_country(country)
        best_client = None
        best_amount = 0
        for client in clients_of_country:
            amount = sales_collection.total_amount_by_client(client.client_id)
            if amount > best_amount:
                best_client = client
                best_amount = amount
        top_client_by_country[country] = best_client.name

    # 7. Total de ventas por categoria.

    sales_dicts = list(map(lambda s: s.to_dict(), sales))
    df = pd.DataFrame(sales_dicts)
    sales_by_category = df.groupby("category")["amount"].sum()
    sales_by_category_dict = sales_by_category.to_dict()

    # 8. Cliente con más ventas en una categoría específica.

    category = "Electronics"
    sales_in_category = filter_sales_by_category(sales, category)
    best_client = None
    best_count = 0
    for client in clients:
        count = 0
        for sale in sales_in_category:
            if sale.client_id == client.client_id:
                count += 1
        if count > best_count:
            best_client = client
            best_count = count

    # 9. Número de clientes que superan un gasto mínimo.
    # Ejemplo: gasto mínimo = 500€

    min_spent = 500
    high_spending_clients = []
    for client in clients:
        spent = sales_collection.total_amount_by_client(client.client_id)
        if spent > min_spent:
            high_spending_clients.append(client.name)

    number_high_spending = len(high_spending_clients)

    # 10. Ventas acumuladas mes a mes.

    dates = pd.to_datetime(df["date"])
    df["month"] = dates.dt.to_period("M").astype(str)
    monthly_sales = df.groupby("month")["amount"].sum().to_dict()

    total_revenue = reduce_total_amount(sales)



    report = {
        "summary": {
            "total_clients": total_clients,
            "total_sales": total_sales,
            "total_revenue": total_revenue,
        },
        "clients": clients_info,
        "top_client_by_country": top_client_by_country,
        "sales_by_category": sales_by_category_dict,
        "high_spending_clients": high_spending_clients,
        "monthly_sales": monthly_sales

    }
    return report










        
    


