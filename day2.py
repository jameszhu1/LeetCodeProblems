#counts the lenght of the last word
class LenLastWordSolution:
    #one Way
    def lengthOfLastWord(self, s):
        counter = 0
        for l in range(len(s) - 1, -1, -1):
            if s[l] != " ":
                counter += 1
            elif counter > 0:
                break
        return counter
    #second way
    '''def lengthOfLastWord(self, s):
        strippedStr = s.strip()
        listOfWords = strippedStr.split(" ")
        return len(listOfWords[-1])'''

q1 = LenLastWordSolution()
print(q1.lengthOfLastWord("James is a beast"))
print(q1.lengthOfLastWord("jjjjjaaaa mmmm  "))
#Plus One
class PlusOneSolution:
    def plusOne(self, digits):
        for i in range(len(digits) - 1, 0, -1):
            digits[i] += 1
            if digits[i] != 10:
                return digits
            digits[i] = 0
        return [1] + digits
q2 = PlusOneSolution()
print(q2.plusOne([2,4,5,9]))
#compute squareroot of a number
class SqrtSolution:
    #Binary SOlution
    def mySqrt(self, x):
        r = x
        l = 0
        while l <= r:
            mid = (l + r) // 2
            if (mid * mid) > x:
                r = mid - 1
            elif (mid * mid) < x:
                l = mid + 1
            else:
                return mid
        return r
    #simple solution
    '''def mySqrt(self, x):
        return int(x**0.5)'''
q3 = SqrtSolution()
print(q3.mySqrt(15))
#max subarray
class maxSubArraySolution:
    def maxSubArray(self, nums):
        maxNum = [0] * len(nums)
        maxNum[0] = nums[0]
        for i in range(1, len(nums)):
            maxNum[i] = max(maxNum[i - 1] + nums[i], nums[i])
            print(maxNum[i])
        return max(maxNum)
q4 = maxSubArraySolution()
print(q4.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
