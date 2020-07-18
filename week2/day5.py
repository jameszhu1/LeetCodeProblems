#Two Sum 2 leetcode 167
class TwoSum2Solution:
    def twoSum(self, numbers, target):
        valuesToReturn = {}
        for index, num in enumerate(numbers):
            if target - num in valuesToReturn:
                return [valuesToReturn[target - num], index + 1]
            else:
                valuesToReturn[num] = index + 1

#Majority Element
class MajorityElementSolution:
    def majorityElement(self, nums):
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            if count[num] > len(nums) / 2:
                return num
            else:
                count[num] += 1

#factorial Trailing zeroes
class ZeroCountFactorialSolution:
    def trailingZeroes(self, n):
        zeroCount = 0
        while n > 0:
            n //= 5
            zeroCount += n
        return zeroCount
