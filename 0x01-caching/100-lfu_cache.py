#!/usr/bin/python3
""" LFUCache module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """ Initialize LFUCache
        """
        super().__init__()
        self.frequency = {}
        self.usage_order = OrderedDict()

    def update_usage_order(self, key):
        """ Update the usage order of the keys
        """
        if key in self.usage_order:
            self.usage_order.move_to_end(key)

    def update_frequency(self, key):
        """ Update the frequency of the keys
        """
        if key in self.frequency:
            self.frequency[key] += 1
        else:
            self.frequency[key] = 1

    def evict_least_frequent(self):
        """ Evict the least frequent key(s)
        """
        min_frequency = min(self.frequency.values())
        least_frequent_keys = [k for k, v in self.frequency.items() if v == min_frequency]
        least_recently_used_key = next(iter(self.usage_order))
        for key in self.usage_order:
            if key in least_frequent_keys:
                least_recently_used_key = key
                break
        del self.cache_data[least_recently_used_key]
        del self.frequency[least_recently_used_key]
        del self.usage_order[least_recently_used_key]
        print("DISCARD: {}".format(least_recently_used_key))

    def put(self, key, item):
        """ Add an item to the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= self.MAX_ITEMS:
                    self.evict_least_frequent()
                self.cache_data[key] = item
                self.update_frequency(key)
                self.usage_order[key] = True

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.update_frequency(key)
            self.update_usage_order(key)
            return self.cache_data[key]
        return None
