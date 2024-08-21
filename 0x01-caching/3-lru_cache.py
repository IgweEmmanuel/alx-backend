#!/usr/bin/env python3
"""
LIFOCache
"""
BaseCaching = __import__("base_caching").BaseCaching
from collections import OrderedDict
cache = OrderedDict()

class LRUCache(BaseCaching):
    """
    LIFOCache
    """

    def __init__(self):
        """
        Initializer
        """
        super().__init__()
        self.cache = OrderedDict()
        self.cache = self.cache_data
    def put(self, key, item):
        """
        put for key items
        Args:
            key(str): key of dictionary
            item(Any): value of dictionary
        """
        if key is not None and item is not None:
            if len(self.cache) >= BaseCaching.MAX_ITEMS:
                lfu = next(iter(self.cache))
                del self.cache[lfu]
                print(f"DISCARD: {lfu}")
            self.cache[key] = item

    def get(self, key):
        """
        get key
        """
        if key is None or key not in self.cache:
            return None
        return self.cache[key]
