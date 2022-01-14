# -*- coding: utf-8 -*-
import requests


class Requests:
    def request(self, url, method="get", **kwargs):
        if method == "get":
            return requests.request(url=url, method=method, **kwargs)
        elif method == "post":
            return requests.request(url=url, method=method, **kwargs)
        elif method == "put":
            return requests.request(url=url, method=method, **kwargs)
        elif method == "patch":
            return requests.request(url=url, method=method, **kwargs)
        elif method == "delete":
            return requests.request(url=url, method=method, **kwargs)

    def get(self, url, **kwargs):
        return self.request(url=url, method="get", **kwargs)

    def post(self, url, **kwargs):
        return self.request(url=url, method="post", **kwargs)

    def put(self, url, **kwargs):
        return self.request(url=url, method="put", **kwargs)

    def patch(self, url, **kwargs):
        return self.request(url=url, method="patch", **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url=url, method="delete", **kwargs)


req = Requests()