class ClientCollection:
    def __init__(self, clients: list):
        self.clients = clients

    # Devuelve un cliente concreto.
    def get_client_by_id(self, id: int):
        for client in self.clients:
            if client.client_id == id:
                return client
        return None  
          
    # Devuelve lista de cliente de un país.
    def clients_by_country(self, country: str):
        filtered_clients = []
        for client in self.clients:
            if client.country == country:
                filtered_clients.append(client)
        return filtered_clients
             
                
        