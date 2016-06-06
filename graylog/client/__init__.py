import requests
from requests.auth import HTTPBasicAuth


class Graylog(object):
    def __init__(self, host='localhost', port='12900',
                 protocol='http', auth={}):
        self.username = auth['username']
        self.auth = HTTPBasicAuth(auth['username'], auth['password'])
        self.uri = protocol + '://' + host + ':' + port
        self.connection_check()

    def connection_check(self):
        r = requests.get(self.uri + '/users/' + self.username, auth=self.auth)
        assert (r.status_code == 200), "Connection failed! : " + str(r)
        return True
