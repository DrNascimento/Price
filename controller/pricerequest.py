import requests

from useful.Retorno import Retorno


class PriceRequest:

    def get_uri(self):
        return self.__uri

    def set_uri(self, uri):
        self.__uri = uri

    def get_requested_uri(self):
        return self.__requested_uri

    def set_requested_uri(self, uri_requested):
        self.__requested_uri = uri_requested

    def get_coin(self):
        return self.__coin

    def set_coin(self, coin):
        self.__coin = coin

    def get_method(self):
        return self.__method

    def set_method(self, method):
        self.__method = method

    def get_result(self):
        return self.__result

    def set_result(self, result):
        self.__result = result

    def __init__(self):
        self.__method = None
        self.__result = None
        self.__coin = None
        self.__uri = "https://www.mercadobitcoin.net/api"
        self.__requested_uri = None

    def request(self, coin, method):
        self.set_coin(coin)
        self.set_method(method)
        self.set_requested_uri(self.get_uri() + "/" + coin + "/" + method)
        return requests.get(self.get_requested_uri())

    def call_request(self, coin="BTC", method="ticker"):
        r = self.request(coin, method)
        if r.status_code == 200:
            Retorno.data = r.json()
            Retorno.error = 0
            Retorno.message = "Requisição bem sucedida"
        else:
            Retorno.data = r.text
            Retorno.error = 1
            Retorno.message = "Requisição mal sucedida"

        Retorno.name_function = f"Método: PriceRequest.call_request. Link utilizado: {self.__requested_uri}"
        self.set_result(Retorno)
        return self.get_result()

    def on_result(self):
        print("oi")
