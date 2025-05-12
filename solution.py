from itertools import permutations
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = set() #we take set to sort out unique elements
        for p in permutations(nums):
            perms.add(p) #we simply add permutations
        return [list(p) for p in perms] #we convert each permutaions into a list

#currently working on this library in future gain knowledge about doing permutations without any usage of libaries :)
