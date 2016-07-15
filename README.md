The LRU Cache is an in memory cache that can be run from the console as ```./console_client.py``` on mac or linux
and ```python console_client.py``` on Windows.

A cache must first be instantiated by provided the size as follows:
```SIZE 3```
Size is limited to max int or 2147483647.

A cache item can be set by using the set command and the contents of a cache key can be retrieved with the get command.
```
SET foo bar
SET boop
GET foo
GOT bar
GET boop
NOTFOUND
```

If a cache goes over the size given the least used key will be removed. The least used key is the key that was set or get
least recently.

To exit and destroy the cache type `EXIT`
