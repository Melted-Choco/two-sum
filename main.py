from typing import List

def twoSum(nums : List[int], target: int) -> List[int]:
    l = len(nums) # length of input list
    list = [] # result list
    for i in range(l): # i : start point of iterating list 'nums'
        sum = 0
        index = i
        list.clear()
        for n in nums[i:]:
            sum += n
            list.append(index)
            index += 1
            if sum == target:
                return list
