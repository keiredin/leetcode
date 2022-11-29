class RandomizedSet:

    def __init__(self):
        self.data_map = {} 
        self.data = [] 

    def insert(self, val: int) -> bool:

        if val in self.data_map:
            return False

    
        self.data_map[val] = len(self.data)

        # add to the list
        self.data.append(val)
        
        return True

    def remove(self, val: int) -> bool:

        if not val in self.data_map:
            return False
        
        last_elem_in_list = self.data[-1]
        index_of_elem_to_remove = self.data_map[val]

        self.data_map[last_elem_in_list] = index_of_elem_to_remove
        self.data[index_of_elem_to_remove] = last_elem_in_list

      
        self.data[-1] = val

        # remove the last element in the list
        self.data.pop()

        # remove the element to be removed from the dictionary
        self.data_map.pop(val)
        return True

    def getRandom(self) -> int:
        # if running outside of leetcode, you need to `import random`.
        # random.choice will randomly select an element from the list of data.
        return random.choice(self.data)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()