"""
:author: Gatsby Lee
:since: 2019-07-15
"""
import requests


API_ENDPOINT = 'http://%(hostname)s/api/v1.0'

class FreenasRestAPiCient(object):


    def __init__(self, hostname, username, password):
        self.auth_tuple = (username, password)
        self.api_endpoint = API_ENDPOINT % {'hostname': hostname}


    def get(self, resource, method='GET', data=None):
        uri = '%s/%s/' % (self.api_endpoint, resource)
        r = requests.get(
            uri,
            headers={'Content-Type': "application/json"},
            auth=self.auth_tuple,
        )

        if r.ok:
            try:
                return r.json()
            except:
                return r.text
        raise ValueError(r)
