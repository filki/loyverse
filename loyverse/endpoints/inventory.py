"""

Inventory endpoint wrapper class
"""

from loyverse.api import Api


class Inventory:
    def __init__(self, api: Api):
        self._api = api
        self._path = "inventory"

    def get_all(self):
        """
        Retrieves all inventory
        """
        return self._api.request("GET", self._path)
