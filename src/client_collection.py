class ClientCollection:
    def __init__(self, clients: list):
        self.clients = clients

    def get_client_by_id(self, id: int):
        for client in self.clients:
            if client.client_id == id:
                return client
        return None        
    
    def clients_by_country(self, country: str):
        filtered_clients = []
        for client in self.clients:
            if client.country == country:
                filtered_clients.append(client)
        return filtered_clients
             
                
        