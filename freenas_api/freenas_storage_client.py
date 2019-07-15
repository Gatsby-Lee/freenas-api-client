"""
:author: Gatsby Lee
:since: 2019-07-15
"""
from freenas_api import FreenasRestAPiCient


class FreenasStorageClient(object):

    def __init__(self, hostname, username, password):

        self._client = FreenasRestAPiCient(hostname, username, password)

    def get_volumes(self):
        """Return volume list"""

        return self._client.get('storage/volume/')

    def get_volume_by_name(self, volume_name):
        """Return volume by volume_name

        Args:
            volume_name str
        Returns: dict
        """

        # resource = 'storage/volume/%s/datasets/' % volume_name
        resource = 'storage/volume/%s/' % volume_name
        return self._client.get(resource)
