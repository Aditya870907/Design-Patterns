from http.http_request_builder import HttpRequestBuilder

class Client:
    @staticmethod
    def main():
        request1 = (
            HttpRequestBuilder("https://api.example.com/data")
            .build()
        )
        print(request1)

        request2 = (
            HttpRequestBuilder("https://api.example.com/submit")
            .method("POST")
            .header("Content-Type", "application/json")
            .body("{\"name\": \"John\", \"age\": 30}")
            .timeout(10000)
            .build()
        )
        print(request2)

        request3 = (
            HttpRequestBuilder("https://api.example.com/config")
            .method("PUT")
            .header("X-API-Key", "super_secret_key")
            .params("version", "1.0.0")
            .body("{\"theme\": \"dark\"}")
            .timeout(5000)
            .build()
        )
        print(request3)

if __name__ == "__main__":
    Client.main()