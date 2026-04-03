"""

"""
from loyverse.api import Api
class Categories():
    def __init__(self, api: Api):
        self._api = api
        self._path = 'categories'

    def get_all(self):
        """
        Retrieves all categories
        """
        return self._api.request('GET', self._path)