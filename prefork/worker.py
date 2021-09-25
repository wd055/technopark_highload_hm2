import asyncio
import atexit
import logging
import multiprocessing
import random
import socket

import uvloop as uvloop

from utils import consts, request, response

logger = logging.getLogger('server')
logger.setLevel(logging.INFO)
logging.basicConfig(format='%(asctime)s %(message)s')


class Worker:
    def __init__(self, sock):
        self.ev_loop = asyncio.get_event_loop()
        self.socket = sock
        self.request = None
        self.response = None

    async def handle_conn(self, conn):
        in_buffer = ""
        while True:
            part = (await asyncio.get_event_loop().sock_recv(conn, 1024)).decode()
            in_buffer += part
            if consts.SEP in in_buffer or len(part) == 0:
                break

        self.request = request.Request(in_buffer)
        result_code = self.request.parse_request()
        self.response = response.Response(
            self.request.method, self.request.url, self.request.protocol, self.request.filepath, result_code)
        await self.response.send(conn, self.ev_loop)

    async def accept_conn(self):
        while True:
            number = random.randint(1, 1000)
            print("FF", number)
            child_conn, _ = await asyncio.get_event_loop().sock_accept(self.socket)
            print("SS", number)
            await self.handle_conn(child_conn)
            self.socket.close()

    def run(self):
        asyncio.run(self.accept_conn())
