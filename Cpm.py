import requests
from time import sleep
BASE_URL: str = "https://cpmelsedevshop.squareweb.app/api"

class CPMElsedev:

    def __init__(self, access_key) -> None:
        self.auth_token = None
        self.access_key = access_key
        self.unlimited_balance = True  # Unlimited balance by default
        self.unlimited_access_key = True  # Unlimited access key

    def login(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/account_login", params=params, data=payload)
        response_decoded = response.json()
        if response_decoded.get("ok"):
            self.auth_token = response_decoded.get("auth")
        return response_decoded.get("error")
    
    def register(self, email, password) -> int:
        payload = { "account_email": email, "account_password": password }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/account_register", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("error")
    
    def delete(self):
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        requests.post(f"{BASE_URL}/account_delete", params=params, data=payload)

    def get_player_data(self) -> any:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/get_data", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded
    
    def set_player_rank(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_rank", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def get_key_data(self) -> any:
        # Skip access key validation since it's unlimited
        params = { "key": self.access_key }
        response = requests.get(f"{BASE_URL}/get_key_data", params=params)
        response_decoded = response.json()
        return response_decoded
    
    def set_player_money(self, amount) -> bool:
        if self.unlimited_balance:
            amount = 9999999999  # Example of setting unlimited money
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_money", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_coins(self, amount) -> bool:
        if self.unlimited_balance:
            amount = 9999999999  # Example of setting unlimited coins
        payload = {
            "account_auth": self.auth_token,
            "amount": amount
        }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_coins", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_name(self, name) -> bool:
        payload = { "account_auth": self.auth_token, "name": name }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_name", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
    
    def set_player_localid(self, id) -> bool:
        payload = { "account_auth": self.auth_token, "id": id }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/set_id", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    # More methods for unlocking items, handling player stats, etc., are similar.
    # Just ensure that whenever it involves balance or access key, 
    # you account for the "unlimited" flags as needed.

    def unlock_all_cars(self) -> bool:
        payload = { "account_auth": self.auth_token }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/unlock_all_cars", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")

    def account_clone(self, account_email, account_password) -> bool:
        payload = { "account_auth": self.auth_token, "account_email": account_email, "account_password": account_password }
        params = { "key": self.access_key }
        response = requests.post(f"{BASE_URL}/clone", params=params, data=payload)
        response_decoded = response.json()
        return response_decoded.get("ok")
      
