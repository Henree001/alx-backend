#!/usr/bin/python3
""" LifoCache module
"""
import base_caching


class LIFOCache(base_caching.BaseCaching):
    """LifoCache  class that inherits from BaseCaching
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
                last = list(self.cache_data.keys())[-1]
                self.cache_data.pop(last)
                print("DISCARD: {}".format(last))
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
