import json
import requests



class APIException(Exception):
    def __init__(self, message):
        self.message = message



class CurrencyConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount: float):
        url = f"https://api.exchangerate-api.com/v4/latest/{base}"
        response = requests.get(url)
        data = json.loads(response.text)
        if 'error' in data:
            raise Exception(data['error'])
        if quote not in data['rates']:
            raise Exception(f"Invalid currency: {quote}")
        return round(data['rates'][quote] * amount, 2)
