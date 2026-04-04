"""
The Client class encapsulates the endpoints of the Loyverse API and provides a single point of initialization for
API requests.

The Client class exposes the following end-points

* receipts
* customers
"""

from loyverse.api import Api
from typing import Optional


class Client:
    """Loyverse API client

    Args:
        access_token (str): Access token string to be used to initialize the client
    """

    def __init__(self, access_token: Optional[str] = None):

        self._api = Api(access_token=access_token)

        self._categories = None
        self._customers = None
        self._discounts = None
        self._employees = None
        self._inventory = None
        self._items = None
        self._merchants = None
        self._modifiers = None
        self._payments = None
        self._pos_devices = None
        self._receipts = None
        self._shifts = None
        self._stores = None
        self._suppliers = None
        self._taxes = None
        self._variants = None

    def request(self, method: str, path: str, params: Optional[dict] = None):
        """
        Client general request
        """

        return self._api.request(method, path, params=params)

    @property
    def customers(self):
        """
        Customers endpoint

        Returns:
            customers (loyverse.endpoints.Customer): Customer endpoint wrapper
        """

        if self._customers is None:
            from loyverse.endpoints import Customers

            self._customers = Customers(self._api)
        return self._customers

    @property
    def receipts(self):
        """
        Receipts endpoint

        Returns:
            receipts (loyverse.endpoints.Receipts): Receipts endpoint wrapper
        """

        if self._receipts is None:
            from loyverse.endpoints import Receipts

            self._receipts = Receipts(self._api)

        return self._receipts

    @property
    def categories(self):
        """
        Categories endpoint

        Returns:
            categories (loyverse.endpoints.Categories): Categories endpoint wrapper
        """

        if self._categories is None:
            from loyverse.endpoints import Categories

            self._categories = Categories(self._api)

        return self._categories

    @property
    def inventory(self):
        """
        Inventory endpoint

        Returns:
            inventory (loyverse.endpoints.Inventory): Inventory endpoint wrapper
        """

        if self._inventory is None:
            from loyverse.endpoints import Inventory

            self._inventory = Inventory(self._api)

        return self._inventory

    @property
    def items(self):
        """
        Items endpoint

        Returns:
            items (loyverse.endpoints.Items): Items endpoint wrapper
        """

        if self._items is None:
            from loyverse.endpoints import Items

            self._items = Items(self._api)

        return self._items
