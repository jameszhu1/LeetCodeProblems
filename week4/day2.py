#move zeroes leetcode 283
class MoveZeroesSolution:
    def moveZeroes(self, nums):
        pos = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1


#does string match the pattern? leetcode 290
class WordPatternSolution:
    def wordPattern(self, pattern, str):
        char_dict = {}
        word_dict = {}

        words = str.split(" ")

        if len(words) != len(pattern):
            return False
        for c, w in zip(pattern, words):
            if c not in char_dict:
                if w in word_dict:
                    return False
                else:
                    char_dict[c] = w
                    word_dict[w] = c
            else:
                if char_dict[c] != w:
                    return False
        return True

#Nim game leetcode 292
class NimSolution:
    def canWinNim(self, n):
        if n % 4 != 0:
            return True
        return False

#is num a power of 3? leetcode 326
class PowerOfThreeSolution:
    def isPowerOfThree(self, n):
        if n == 0:
            return False
        if n == 1:
            return True
        if n > 1:
            return n % 3 == 0 and self.isPowerOfThree(n / 3)
        else:
            return False

#reverse string in place with no extra space leetcode 344
class ReverseStringSolution:
    def reverseString(self, s):
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -=1
