# 2023-12-01 
# LeetCode 1662. Check If Two String Arrays are Equivalent
class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(word1) == ''.join(word2)
        # a = ''.join(word1)
        # b = ''.join(word2)

        # if a==b: return True
        # else: return False
        