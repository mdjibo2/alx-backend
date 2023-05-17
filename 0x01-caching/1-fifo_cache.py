#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize FIFOCache
        """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    discarded_key = self.queue.pop(0)
                    del self.cache_data[discarded_key]
                    print("DISCARD: {}".format(discarded_key))
                self.cache_data[key] = item
                self.queue.append(key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
