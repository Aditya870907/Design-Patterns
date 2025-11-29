class HttpRequest:
    def __init__(self, url, method, headers, query_params, body, timeout):
        self.url = url
        self.method = method
        self.headers = headers
        self.query_params = query_params
        self.body = body
        self.timeout = timeout
    
    def __str__(self):
        return (
            f"HttpRequest(url={self.url},"
            f"method={self.method},"
            f"headers={self.headers},"
            f"query_params={self.query_params},"
            f"body={self.body},"
            f"timeout={self.timeout})"
        )