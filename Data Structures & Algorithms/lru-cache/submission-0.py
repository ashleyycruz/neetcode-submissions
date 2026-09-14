class LRUCache:

    def __init__(self, capacity: int):
            
        # Inititalize the LRU cashe of size (capacity) & store 
        self.capacity = capacity
        self.store = {}
         
    def get(self, key: int) -> int:

        # get 
        # update the value of the key ( if exists ) 
        # if new key: add a new (key,value) pair to the cache

        if key not in self.store: 
            return -1  # otherwise return -1 ( doesn't exists )

        value = self.store.pop(key)
        self.store[key] = value  # marks it as recently used

        return value    

    def put(self, key: int, value: int) -> None:
        
        # if already there pop  
        if key in self.store:
            self.store.pop(key)

        # add if new ( become more recent )
        self.store[key] = value

        # if execeeded capaity ( FIFO ) remove the least recently used key
        if len(self.store) > self.capacity:
            least_recent_key = next(iter(self.store))
            self.store.pop(least_recent_key)

        return None   