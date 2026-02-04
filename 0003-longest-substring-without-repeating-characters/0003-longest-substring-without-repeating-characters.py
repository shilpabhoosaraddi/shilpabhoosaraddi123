class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl=0
        left=0
        uniqset = set()
        for right in range(0,len(s)):
            if s[right] not in uniqset:
                uniqset.add(s[right])
                maxl=max(maxl,right-left+1)
            else:
                while s[right] in uniqset:
                    uniqset.remove(s[left])
                    left+=1
                uniqset.add(s[right])
                maxl=max(maxl,right-left+1)
        return maxl
    