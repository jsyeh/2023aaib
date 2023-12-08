# LeetCode 1688. Count of Matches in Tournament
# 這題很像是「模擬比賽對決」的晉級模擬。偶數要對戰 n//2 場, 奇數則是 (n-1)//2 場
# 持續比, 直到冠軍出來。
# 因為是淘汰賽,n隊的話,只要比n-1場,就淘汰其他隊, 就得冠軍了
class Solution:
    def numberOfMatches(self, n: int) -> int:
        return n-1