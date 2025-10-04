# Two sum
def two_sum(nums, target):
    lookup = {}
    for ind, num in enumerate(nums):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], ind]
        else:
            lookup[num] = ind
    return []
#Time complexity:O(n), Space complexity:O(n)
"""
nums = [2, 7, 11, 15]
target = 13

print(two_sum(nums, target))
"""


def if_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def contains_duplicate(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False

def is_anagram(s, t):
    return sorted(s) == sorted(t)
#O(nlogn),O(n) 
#sorted use new space


def is_anagram3(s, t):
    if len(s) != len(t):
        return False
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    for cha in t:
        if cha not in freq:
            return False
        else:
            freq[cha] -= 1
            if freq[cha] < 0:
                return False
    return True
#O(n), O(1) only 26 letters