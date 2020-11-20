#!/usr/bin/env python3


import requests
import json
from monnamon.utils import validate_data


def get_auth_token(consumer_id: str, secret_key: str) -> str:

    url = 'https://prewservices.afripayway.com/api/gateway/operations/v1/authenticate'
    headers = {'Content-type': 'application/json', 'consumerId': consumer_id, 'secretKey': secret_key}
    req = requests.post(url, headers=headers)
    response = req.json()
    return response['message']


@validate_data
def create_cash_wallet_transaction(auth_token, data: dict):
    print('OK')
    
