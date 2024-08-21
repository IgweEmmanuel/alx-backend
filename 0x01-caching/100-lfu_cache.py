#!/usr/bin/env python3
"""
LFUCache
"""
BaseCaching = __import__("base_caching").BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache
    """

    def __init__(self):
        """
        Initializer
        """
        super().__init__()
        self.hold = []
        self.freq = {}

    def put(self, key, item):
        """
        put for key items
        Args:
            key(str): key of dictionary
            item(Any): value of dictionary
        """
        if key in self.cache_data:
            self.hold.remove(key)
            self.freq[key] += 1
            self.cache_data[key] = item

        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                lfu = min(self.freq.values())
                count = [k for k, v in self.freq.items() if v == lfu]
                if len(count) > 1:
                    lfu = None
                    for k in self.hold:
                        if k in count:
                            lfu = k
                            break
                else:
                    lfu = count[0]
                self.cache_data.pop(lfu)
                self.freq.pop(lfu)
                self.hold.remove(lfu)
                print(f"DISCARD: {lfu}")
            self.cache_data[key] = item
            self.freq[key] = 1
        self.hold.append(key)

    def get(self, key):
        """
        get key
        """
        if key is None or key not in self.cache_data:
            return None
        self.freq[key] += 1
        self.hold.remove(key)
        self.hold.append(key)
        return self.cache_data[key]
