class RandomizedSet:

    def __init__(self):
        self.random_map = {}
        self.random_list = []

    def insert(self, val: int) -> bool:
        if val in self.random_map:
            return False
        self.random_map[val] = len(self.random_list)
        self.random_list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.random_map:
            return False

        last_value = self.random_list[-1]
        val_idx = self.random_map[val]
        self.random_list[val_idx] = last_value
        self.random_map[last_value] = val_idx

        self.random_list.pop()
        del self.random_map[val]
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.random_list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()