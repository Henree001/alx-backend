#!/usr/bin/python3
""" FifoCache module
"""
import base_caching


class FIFOCache(base_caching.BaseCaching):
    """FifoCache  class that inherits from BaseCaching
    """
    def __init__(self):
        """ Init
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= self.MAX_ITEMS:
                first = list(self.cache_data.keys())[0]
                self.cache_data.pop(first)
                print("DISCARD: {}".format(first))
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
