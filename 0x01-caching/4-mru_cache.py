#!/usr/bin/python3
""" MRU Cache module
"""
import base_caching


class MRUCache(base_caching.BaseCaching):
    """MRU Cache  class that inherits from BaseCaching
    """
    def __init__(self):
        """ Init
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= self.MAX_ITEMS:
                last = self.order.pop(-1)
                self.cache_data.pop(last)
                print("DISCARD: {}".format(last))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
