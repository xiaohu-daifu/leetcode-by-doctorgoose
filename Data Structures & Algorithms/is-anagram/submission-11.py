class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            dicts[s[i]] = 1 + dicts.get(s[i], 0)  
            dictt[t[i]] = 1 + dictt.get(t[i], 0) 

        return dicts == dictt