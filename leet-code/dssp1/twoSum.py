class Solution:
    def twoSum(self, nums, target):
        index = {}
        
        for i, elem in enumerate(nums):
            if elem in index:
                index[elem].append(i)
            else:
                index[elem] = [i]
        
        for i, elem in enumerate(nums):
            x = target - elem
            
            if x in index:
                if index[x][0] != i:
                    return [index[x][0], i]
                elif len(index[x]) > 1:
                    return [index[x][0], index[x][1]]