import json
import pprint
import socket
import time


class SocketClient:

    def __init__(self, target_host='127.0.0.1', target_port=5000) -> None:
        self.target_host = target_host
        self.target_port = target_port
        self.client = None
        self.data = None

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.settimeout(0.1)
        self.client.connect((self.target_host, self.target_port))

    def disconnect(self):
        self.client.close()

    def get(self, params):
        request = f'GET {params} HTTP/1.1\r\nHost:{self.target_host}\r\n\r\n'
        self.client.send(request.encode())

    def post(self, params, data):
        body = f'author={data["author"]}&name={data["name"]}'
        request = f'POST {params} HTTP/1.1\r\n' \
                  f'Content-Type: application/x-www-form-urlencoded\r\n' \
                  f'Content-Length: {len(body)}\r\n\r\n' \
                  f'{body}'
        self.client.send(request.encode())

    def receive(self):
        tmp = []
        while True:
            data = self.client.recv(4096)
            if data:
                tmp.append(data.decode())
            else:
                break
        splitted_data = ''.join(tmp).splitlines()
        code = splitted_data[0].split()[1]
        if code == '200':
            self.data = {'status_code': int(code), 'headers': splitted_data[:-1],
                         'data': json.loads(splitted_data[-1])}
        else:
            self.data = {'status_code': int(code), 'headers': splitted_data[:-1],
                         'data': None}
        return self.data


if __name__ == '__main__':
    client = SocketClient()
    time.sleep(1)
    client.connect()
    client.post('/new_book', {'author': 'Mark Twen', 'name': 'The Adventures of Tom Sawyer'})
    pprint.pprint(client.receive())
    client.disconnect()

    client.connect()
    client.post('/new_book', {'author': 'Mario Puzo', 'name': 'The Godfather'})
    pprint.pprint(client.receive())
    client.disconnect()

    client.connect()
    client.get('/books')
    pprint.pprint(client.receive())
    client.disconnect()

    client.connect()
    client.get('/shutdown')
    client.disconnect()
