#find target from index addition
class Solution2sum:
    def twoSum(self, nums, target):
        found = {}
        for i, n in enumerate(nums):
            if target - n in found:
                return [found[target - n], i]
            found[n] = i

q1 = Solution2sum()
print(q1.twoSum([2, 7, 11, 15], 9))
#Reverse an integer
class SolutionRevInteger:
    def reverse(self, x):
        if x >= (2**31) - 1 or x <= -2**31:
            return 0
        else:
            intToStr = str(x)
            if x >= 0:
                reverseStr = intToStr[::-1]
            else:
                noNeg = intToStr[1:]
                reverse_noNeg = noNeg[:: -1]
                reverseStr = "-" + reverse_noNeg
            if int(reverseStr) >= (2 ** 31) - 1 or int(reverseStr) <= -2**31:
                return 0
            else:
                return int(reverseStr)
q2 = SolutionRevInteger()
print(q2.reverse(-123))
print(q2.reverse(120))
#Find Palindrome number
class SolutionPalindromeNum:
    def isPalindrome(self, x):
        StrInt = str(x)
        if StrInt == StrInt[::-1]:
            return True
        else:
            return False
q3 = SolutionPalindromeNum()
print(q3.isPalindrome(121))
print(q3.isPalindrome(-565))
#Turn Roman numbers to Integers
class SolutionRomanInt:
    def romanToInt(self, s):
        romanNumDict ={
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        num = 0
        prev = 0
        for i in s[::-1]:
            if romanNumDict[i] >= prev:
                num += romanNumDict[i]
            else:
                num -= romanNumDict[i]
            prev = romanNumDict[i]
        return num
q4 = SolutionRomanInt()
print(q4.romanToInt("CM"))
print(q4.romanToInt("LVIII"))
print(q4.romanToInt("IX"))
#Find the longet prefix of a string
class SolutionPrefix:
    def longestCommonPrefix(self, strs):
        lcp = ""
        unpack = zip(*strs)
        for c in unpack:
            if len(set(c)) > 1:
                break
            lcp += c[0]
        return lcp
q5 = SolutionPrefix()
print(q5.longestCommonPrefix(["james", "jamuis", "jams", "jaming"]))
#Respective brackets
class SolutionBracket:
    def isValid(self, s):
        stack = []
        for c in s:
            if c == "{" or c == "[" or c == "(":
                stack.append(c)
            elif len(stack) <= 0:
                return False
            elif c == ")" and stack.pop() != "(":
                return False
            elif c == "}" and stack.pop() != "{":
                return False
            elif c == "]" and stack.pop() != "[":
                return False
        if len(stack) == 0:
            return True
        return False
q6 = SolutionBracket()
print(q6.isValid("(){}[]"))
print(q6.isValid("{[(}]}"))
#Merge 2 sorted linked lists
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class SolutionLL:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        head = dummy
        while l1 and l2:
            if l1.val < l2.val:
                dummy.next = l1
                l1 = l1.next
            else:
                dummy.next = l2
                l2 = l2.next
            dummy = dummy.next
        dummy.next = l1 or l2
        return head.next

    def mergeTwoListsRecursive(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoListsRecursive(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoListsRecursive(l1, l2.next)
            return l2
#Remove duplicates
class SolutionRmDup:
    def removeDuplicates(self, nums):
        for n in range(len(nums) - 1, 0, -1):
            if nums[n] == nums[n - 1]:
                del nums[n]
        return nums

q8 = SolutionRmDup()
print(q8.removeDuplicates([6, 6, 3, 3 ,3, 2, 1]))
#Remove Elements in place
class SolutionRmElements:
    def removeElements(self, nums, val):
        while True:
            try:
                nums.remove(val)
            except ValueError:
                break
        return len(nums)
q9 = SolutionRmElements()
print(q9.removeElements([1,1,1,2,3,4,4,3,3], 1))
#Return index of the first occurence of needle in haystack
class SolutionNeedleHaystack:
    def strStr(self, haystack, needle):
        return haystack.find(needle)
q10 = SolutionNeedleHaystack()
print(q10.strStr("hello", "ll"))
print(q10.strStr("james", "aa"))
#Search target value in sorted array and return index
class SolutionSearch:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if target > nums[mid]:
                left = mid + 1
            else:
                right = mid
        return left
q11 = SolutionSearch()
print(q11.searchInsert([3, 6, 7, 8, 9], 5))
