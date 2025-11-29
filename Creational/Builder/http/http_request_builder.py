from .http_request import HttpRequest

class HttpRequestBuilder:
    def __init__(self, url):
        self._url = url
        self._method = "GET"
        self._header = {}
        self._params = {}
        self._body = None
        self._timeout = 30000
    
    def method(self, method: str):
        self._method = method
        return self
    
    def headers(self, key, value):
        self._header[key] = value
        return self
    
    def params(self, key, value):
        self._params[key] = value
        return self
    
    def body(self, body):
        self._body = body
        return self
    
    def timeout(self, ms: int):
        self._timeout = ms
        return self
    
    def build(self) -> HttpRequest:
        return HttpRequest(
            url = self._url,
            method = self._method,
            headers = self._header,
            query_params = self._params,
            body = self._body.
            timeout = self._timeout
        )