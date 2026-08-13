class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        from itertools import combinations
        i_values = [i for i in range(0, len(nums))]
        
        zipped_i_nums = zip(i_values, nums)
        comb_nums = combinations(list(zipped_i_nums), 2)

        for ele in list(comb_nums):
            sum = (lambda x: x[0][1] + x[1][1])(ele)
            if sum == target:
                return [ele[0][0], ele[1][0]]
            