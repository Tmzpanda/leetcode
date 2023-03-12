# 380. RandomizedSet Insert Delete GetRandom O(1) 
class RandomizedSet:
    def __init__(self):
        self.nums = []
        self.val_to_index = {}

    def insert(self, val: int) -> bool:
        if val in self.val_to_index:
            return False
        
        self.nums.append(val)
        self.val_to_index[val] = len(self.nums) - 1
        return True 

    def remove(self, val: int) -> bool:         # O(1) remove in an array
        if val not in self.val_to_index:
            return False
        
        index = self.val_to_index[val]
        last_value = self.nums[-1]
        
        self.nums[index] = last_value
        self.val_to_index[last_value] = index
        self.nums.pop()
        del self.val_to_index[val]
        
        return True
        
    def getRandom(self) -> int:
        return self.nums[random.randint(0, len(self.nums) - 1)]    
    
    