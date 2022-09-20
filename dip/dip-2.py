import requests

class Connection:
    def __init__(self, base_url, **kwargs):
        self.base_url = base_url

    def get(self, url, **kwargs):
        raise NotImplementedError

    def post(self, url, **kwargs):
        raise NotImplementedError

class RequestsApi(Connection):
    def __init__(self, base_url, **kwargs):
        self.session = requests.Session()
        for arg in kwargs:
            if isinstance(kwargs[arg], dict):
                kwargs[arg] = self.__deep_merge(getattr(self.session, arg), kwargs[arg])
            setattr(self.session, arg, kwargs[arg])

    def request(self, method, url, **kwargs):
        return self.session.request(method, self.base_url+url, **kwargs)

    def head(self, url, **kwargs):
        return self.session.head(self.base_url+url, **kwargs)

    def get(self, url, **kwargs):
        return self.session.get(self.base_url+url, **kwargs)

    def post(self, url, **kwargs):
        return self.session.post(self.base_url+url, **kwargs)



class SiteConnection:

    def __init__(self, requestApi: Connection, **kwargs):
        self.request = requestApi

    def subpath(self, path):
        print(self.request.get(path).content)


uol = SiteConnection(RequestsApi('http://www.uol.com.br'))
uol.subpath('/esportes')
