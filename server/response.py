import asyncio
from datetime import datetime
from socket import socket
from utils import consts
from utils import config
import pathlib
import os


class Response:
    def __init__(self, method: str, url: str, protocol: str, filepath: str, code: str):
        self.method = method
        self.url = url
        self.protocol = protocol
        self.filepath = filepath
        self.http_status_code = code
        self.headers = {
            'Connection': 'Close',
            'Server': config.SERVER_NAME,
            'Date': datetime.now().strftime(
                '%a, %d %b %Y %H:%M:%S GMT'),
        }
        self.response = ''

        if self.http_status_code == consts.HTTP_STATUS_OK and self.filepath is not None:
            self.headers['Content-Type'] = consts.CONTENT_TYPES[pathlib.Path(
                self.filepath).suffix]
            self.headers['Content-Length'] = str(
                os.path.getsize(self.filepath))

        self.response = self.protocol + ' ' + str(self.http_status_code) + ' ' + consts.HTTP_STATUS_CODES[
            self.http_status_code] + consts.SEP

        for header, value in self.headers.items():
            self.response += f'{header}: {value}' + consts.SEP
        self.response += consts.SEP

    async def send(self, connect: socket):
        connect.sendall(self.response.encode('utf-8'))
        if self.http_status_code == consts.HTTP_STATUS_OK and self.method == consts.METHOD_GET and self.filepath is not None:
            with open(self.filepath, 'rb') as file:
                part = file.read(1024)
                while len(part) > 0:
                    try:
                        await asyncio.get_event_loop().sock_sendall(connect, part)
                    except Exception as e:
                        print(str(e))
                        return
                    part = file.read(1024)
