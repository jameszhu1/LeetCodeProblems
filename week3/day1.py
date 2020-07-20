#happy number leetcode 202
class HappySolution:
    def isHappy(self, n):
        seen = set()
        while n not in seen:
            seen.add(n)
            n = sum(int(i)**2 for i in str(n))
        return n == 1

#Remove Linked List Element leetcode 203
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class RemovElementSolution:
    def removeElements(self, head, val):
        dummy = ListNode(0)
        dummy.next = head
        node = dummy
        while node.next:
            if node.next.val == val:
                node.next = node.next.next
            else:
                node = node.next
        return dummy.next

#Count Primes leetcode 204
class CountPrimesSolution:
    def countPrimes(self, n):
        listOfPrimes = [True] * n
        primeCount = 0
        if n < 3:
            return 0
        i = 2
        while i * i < n:
            if listOfPrimes[i] == True:
                j = i
                while j * i < n:
                    listOfPrimes[j * i] = False
                    j += 1
            i += 1

        for p in listOfPrimes:
            if p == True:
                primeCount += 1

        return primeCount - 2

#leetcode 205 Isomorphic Strings
class IsomorphicSolution:
    def isIsomorphic(self, s, t):
        lenS = len(s)
        lenT = len(t)
        charMap = {}
        for i in range(lenS):
            if s[i] in charMap:
                if charMap[s[i]] != t[i]:
                    return False
            elif t[i] in charMap.values():
                return False
            else:
                charMap[s[i]] = t[i]
        return True

#Reverse LinkedList leetcode 206
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class ReverseLinkedListSolution:
    def reverseLinedList(self, n):
        prev = None
        cur = head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
