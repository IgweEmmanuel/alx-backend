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

    def put(self, key, item):
        """
        put for key items
        Args:
            key(str): key of dictionary
            item(Any): value of dictionary
        """
        cache = self.cache_data

        if key is not None and item is not None:
            if len(cache) >= BaseCaching.MAX_ITEMS:
                lfu = next(iter(cache))
                del cache[lfu]
                print(f"DISCARD: {lfu}")
            cache[key] = item

    def get(self, key):
        """
        get key
        """
        cache = self.cache_data
        if key is None or key not in cache:
            return None
        return cache[key]
