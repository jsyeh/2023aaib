# 1704. Determine if String Halves Are Alike
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        N = len(s) # 字串的長度 ex. s="textbook"
        a = s[ :N//2] # 前半段      a="text"
        b = s[N//2: ] # 前半段           b="book"
        motherA = 0 # a的母音有幾個
        motherB = 0 # a的母音有幾個
        mother = "aeiouAEIOU"
        for c in a: # 在a裡面的每一個字母 c 逐一檢查
            if c in mother: motherA += 1
        for c in b: # 在b裡面的每一個字母 c 逐一檢查
            if c in mother: motherB += 1
        if motherA == motherB:  return True
        else: return False
        