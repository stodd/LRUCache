class LRUCache:
    def __init__(self, size=3):
        self._size = int(size)
        self._key_recency_list = []
        self._cache_dict = {}

    def get(self, key):
        val = self._cache_dict.get(key)
        # Get also moves an item to the
        if val:
            self._key_recency_list.remove(key)
            self._key_recency_list.append(key)
        return val

    def set(self, key, value):
        if key in self._key_recency_list:
            self._key_recency_list.remove(key)
        self._key_recency_list.append(key)
        self._cache_dict[key] = value
        #Check the size
        if len(self._key_recency_list) >= self._size:
            # By appending and popping 0 the recency list is not a filo queue.
            key_to_remove = self._key_recency_list.pop(0)
            self._cache_dict.pop(key_to_remove, None)
        return (key, value)
