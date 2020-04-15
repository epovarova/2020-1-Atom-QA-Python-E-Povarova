import json
from urllib.parse import urljoin

import requests

from api.urls.urls import Urls


class Client:
    def __init__(self, user, password):
        self.base_url = 'https://target.my.com/'
        self.session = requests.Session()
        self.user = user
        self.password = password
        self.headers = None

    def _request(self, method, location, headers=None, data=None, redirect=False):
        url = urljoin(self.base_url, location)
        return self.session.request(method, url, headers=headers, data=data, allow_redirects=redirect)

    def location_after_auth(self, user, password):
        data = {
            'email': user,
            'password': password,
        }
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            'Referer': self.base_url
        }
        return self._request('POST', Urls.AUTH, data=data, headers=headers).headers['Location']

    def redirects(self):
        z = self._request('GET', Urls.FOR_Z).headers['Set-Cookie'].split(';')[0]
        data = {'email': self.user,
                'password': self.password}
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   'Referer': self.base_url}

        cookies = self._request('POST', Urls.AUTH, data=data, headers=headers).headers['Set-Cookie'].split(';')
        mc = cookies[0]
        ssdc = cookies[7].split()[1]
        mrcu = cookies[14].split()[1]
        headers = {'Cookie': f'{z}; {mc}; {ssdc}; {mrcu}'}

        data = {'headers': headers,
                'Location': self._request('GET', Urls.MY_COM, headers=headers).headers['Location']}

        data = {'headers': data['headers'],
                'Location': self._request('GET', data['Location'], headers=headers).headers['Location']}

        headers['Cookie'] += \
            f"; {self._request('GET', data['Location'], headers=data['headers']).headers['Set-Cookie'].split(';')[0]}"
        return headers

    def login(self):
        headers = self.redirects()
        head = self._request('GET', Urls.CSRF, headers).headers
        headers['Cookie'] += f'; {head["Set-Cookie"]}'

        self.headers = headers

    def create(self, data):
        headers = {
            'Content-Type': 'application/json',
            'Cookie': self.headers['Cookie'],
            'Referer': 'https://target.my.com/segments/segments_list/new',
            'X-CSRFToken': self.headers['Cookie'].split(';')[5].split('=')[-1],
            'X-Requested-With': 'XMLHttpRequest'
        }
        return self._request('POST', Urls.CREATE, headers=headers, data=json.dumps(data))

    def delete(self, id):
        headers = {
            'Cookie': self.headers['Cookie'],
            'Referer': 'https://target.my.com/segments/segments_list',
            'X-CSRFToken': self.headers['Cookie'].split(';')[5].split('=')[-1]
        }
        return self._request("DELETE", Urls.DELETE(id), headers=headers).status_code
