from urllib.parse import unquote
from utils import consts
from utils import config
import os


class Request:
    def __init__(self, raw: str):
        self.raw = raw
        self.method = ''
        self.url = ''
        self.protocol = ''
        self.filepath = None

    def parse_request(self):
        strings = self.raw.split(consts.SEP)
        if strings[0] == '\n' or len(strings) < 3:
            return consts.HTTP_STATUS_FORBIDDEN
        self.method, url, self.protocol = strings[0].split(' ')
        self.url = url
        res = self.validate_method()
        if res != consts.HTTP_STATUS_OK:
            return res
        res = self.validate_url()
        return res

    def validate_url(self):
        self.url = unquote(self.url.split('?')[0])
        if str(self.url).find('/../') > 0:
            print(f'url contains /../')
            return consts.HTTP_STATUS_FORBIDDEN

        filepath = os.path.join(config.DOCUMENT_ROOT, self.url.lstrip('/'))
        if os.path.isdir(filepath):
            filepath = os.path.join(filepath, 'index.html')
            if not os.path.exists(filepath):
                print(f'{filepath} - file not found')
                return consts.HTTP_STATUS_FORBIDDEN
        else:
            if not os.path.isfile(filepath):
                print(f'{filepath} - file not file')
                return consts.HTTP_STATUS_NOTFOUND
        self.filepath = filepath
        return consts.HTTP_STATUS_OK

    def validate_method(self):
        if self.method not in consts.ALLOW_METHODS:
            print(f'{self.method} not allowed')
            return consts.HTTP_STATUS_NOTALLOWED
        return consts.HTTP_STATUS_OK
