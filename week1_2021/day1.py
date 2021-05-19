import functools
import time
 # ---------------------- 2 decorators from https://realpython.com/primer-on-python-decorators/ -----------------
def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug


# ----------------------------------START---------------------------------------------------------------------

#12 integerToRoman
class SolutionIntToRoman:
    @debug
    @timer
    def intToRoman(self, num: 'int') -> 'str':
        d = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }

        res = ""
        for key, value in d.items():
            res += value * (num // key)
            num %= key
        return res


#15 3sum
class SolutionThreeSum:
    @debug
    @timer
    def threeSum(self, nums: 'List[int]') -> 'List[List[int]]':

        nums.sort()
        ret = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                threeSum = nums[i] + nums[left] + nums[right]

                if threeSum == 0:
                    ret.append([nums[i], nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                elif threeSum < 0:
                    left += 1
                else:
                    right -= 1

        return ret




#22 generate parenthesis

class SolutionGenerateParenthesis:
    @debug
    @timer
    def generateParenthesis(self, n: 'int') -> 'List[str]':
        if not n:
            return []
        left, right, ans = n, n, []
        self.dfs(left, right, ans, "")
        return ans
    def dfs(self, left, right, ans, strings):
        if right < left:
            return
        if not left and not right:
            ans.append(strings)
            return
        if left:
            self.dfs(left - 1, right, ans, strings + "(")
        if right:
            self.dfs(left, right - 1, ans, strings + ")")
