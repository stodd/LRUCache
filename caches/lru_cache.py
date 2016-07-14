class LRUCache:
    def __init__(self, size=3):
        self._size = int(size)
        self._key_recency_list = []
        self._cache_dict = {}

    def get(self, key):
        val = self._cache_dict.get(key)
        return val

    def set(self, key, value):
        if key in self._key_recency_list:
            self._key_recency_list.remove(key)
        self._key_recency_list.insert(0, key) #Push
        self._cache_dict[key] = value
        #Check the size
        if len(self._key_recency_list) >= self._size:
            keys_to_remove = self._key_recency_list[self._size:]
            for del_key in keys_to_remove:
                self._cache_dict.pop(del_key, None)
        return (key, value)
