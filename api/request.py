import json

import requests

from flathub.settings import GITHUB, TOKEN

headers = {'Content-type': 'application/json', 'Authorization': 'token {}'.format(TOKEN),
           'accept': 'application/vnd.github.v3+json'}


def to_str(data):
    return str(data).replace('\'', '"')


def get_request(url):
    try:
        return requests.get('{}/{}'.format(GITHUB, url), headers=headers).json()
    except Exception as ex:
        return str(ex)


def patch_request(url, data):
    try:
        request = requests.patch('{}/{}'.format(GITHUB, url), data=to_str(data), headers=headers)
        return {"code": request.status_code, "text": json.loads(request.text)}
    except Exception as ex:
        return str(ex)


def post_request(url, data):
    try:
        request = requests.post('{}/{}'.format(GITHUB, url), data=to_str(data), headers=headers)
        return {"code": request.status_code, "text": json.loads(request.text)}
    except Exception as ex:
        return str(ex)


def put_request(url, data):
    try:
        request = requests.put('{}/{}'.format(GITHUB, url), data=to_str(data), headers=headers)
        return {"code": request.status_code, "text": json.loads(request.text)}
    except Exception as ex:
        return str(ex)


def get_user(login):
    try:
        return requests.get('{}/{}'.format('https://api.github.com/users', login), headers=headers).json()
    except Exception as ex:
        return str(ex)
