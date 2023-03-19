class Solution:
    """
    Description: checks if a number is palindromic
    """
    def isPalindrome(self, x: int) -> bool:
        if x >= 0:
            y = list(str(x))
            y = int(''.join([i for i in reversed(y)]))

            if x == y:
                return True

        return False


if __name__ == "__main__":
    a = Solution()
    print(a.isPalindrome(121))
