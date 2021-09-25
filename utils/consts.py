CONFIG_PATH = '/etc/httpd.conf'

SEP = '\r\n'

METHOD_GET = 'GET'
METHOD_HEAD = 'HEAD'
ALLOW_METHODS = [METHOD_GET, METHOD_HEAD]

HTTP_STATUS_OK = 200
HTTP_STATUS_FORBIDDEN = 403
HTTP_STATUS_NOTFOUND = 404
HTTP_STATUS_NOTALLOWED = 405

HTTP_STATUS_CODES = {
    HTTP_STATUS_OK: 'OK',
    HTTP_STATUS_FORBIDDEN: 'Forbidden',
    HTTP_STATUS_NOTFOUND: 'Not Found',
    HTTP_STATUS_NOTALLOWED: 'Method Not Allowed',
}

CONTENT_TYPES = {
    '.html': 'text/html',
    '.css': 'text/css',
    '.js': 'application/javascript',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.gif': 'image/gif',
    '.swf': 'application/x-shockwave-flash',
}
