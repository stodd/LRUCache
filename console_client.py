#!/usr/bin/python
from caches.lru_cache import LRUCache

cache = None

if __name__ == '__main__':

    command = None
    while command != 'EXIT':
        input = raw_input('')
        input_split = input.split(' ')
        command = input_split[0].upper()

        if command == 'SIZE':
            try:
                cache = LRUCache(input_split[1])
            except:
                print("ERROR")
            else:
                print("SIZE OK")
            continue

        elif command == 'SET':
            val = None
            if len(input_split) == 3:
                val = input_split[2]
            try:
                cache.set(input_split[1], val)
            except Exception as e:
                print("ERROR")
                raise(e)
            else:
                print("SET OK")
            continue

        elif command == 'GET':
            try:
                if len(input_split) > 2:
                    raise
                val = cache.get(input_split[1])
            except:
                print("ERROR")
            else:
                if val:
                    print("GOT %s" % val)
                else:
                    print("NOTFOUND")
            continue

        elif command == 'EXIT':
            continue

        else:
            print("ERROR")