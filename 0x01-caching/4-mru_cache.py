#!/usr/bin/python3
""" MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize MRUCache
        """
        super().__init__()
        self.usage_order = []

    def update_usage_order(self, key):
        """ Update the usage order of the keys
        """
        if key in self.usage_order:
            self.usage_order.remove(key)
        self.usage_order.append(key)

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    discarded_key = self.usage_order.pop()
                    del self.cache_data[discarded_key]
                    print("DISCARD: {}".format(discarded_key))
                self.cache_data[key] = item
                self.update_usage_order(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.update_usage_order(key)
            return self.cache_data[key]
        return None
