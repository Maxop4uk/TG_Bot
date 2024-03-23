import json
import requests
from config import keys

class ConvertionExeption(Exception):
    pass


class Convertion:
    @staticmethod
    def convert_1(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionExeption(f'Невозможно конвертировать одинаковые валюты {quote}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Неудалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Неудалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Неправильное значение {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        price_ticker = json.loads(r.content)[keys[base]]
        total_base = price_ticker*amount
        return total_base
