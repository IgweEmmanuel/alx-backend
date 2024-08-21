#!/usr/bin/python3
""" BaseCaching module
"""
baseCaching = __import__("base_caching").BaseCaching


class BasicCache(baseCaching):
    """
    Basic Cache inheriting from BaseCaching
    """


    def put(self, key, item):
        """
        put key value in dictionary
        Args:
            key(str): the key of the dictionary
            item(Any): the value of the key
        Return:
            This returns dictionary
        """
        if key == None and item == None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        get key values
        Args:
            key(str): this is the key of the dictionary
        Return:
            This retuns value of key
        """
        if key == None or key not in self.cache_data:
            return None
        return self.cache_data[key]
