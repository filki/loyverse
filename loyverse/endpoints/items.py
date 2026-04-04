"""
Items endpoint wrapper class
"""

from loyverse.api import Api


class Items:
    def __init__(self, api: Api):
        self._api = api
        self._path = "items"

    def get_all(self):
        """
        Retrieves all items
        """
        return self._api.request("GET", self._path)

    def get_by_ids(self, item_ids: list):
        """
        Retrieves items information for a specific list of item IDs
        """
        params = {"ids": ",".join(item_ids)}
        return self._api.request("GET", self._path, params=params)

    def get_by_sku(self, sku: str):
        """
        Retrieves items information for a specific SKU
        """
        params = {"sku": sku}
        return self._api.request("GET", self._path, params=params)

    def get_by_category_id(self, category_id: str):
        """
        Retrieves items information for a specific category ID
        """
        params = {"category_id": category_id}
        return self._api.request("GET", self._path, params=params)
