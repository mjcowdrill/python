import requests

from exceptions import ConnectionError


class Account(object):
    def __init__(self, data_interface):
        self.di = data_interface

    def get_current_balance(self, id_num):
        response = requests.get("http://some-account-uri/" + id_num)
        return {'status': response.status_code,
                'data': response.text}

    def get_account(self, id_num):
        try:
            result = self.di.get(id_num)
        except ConnectionError:
            result = "Connection error occurred. Try Again."
        return result