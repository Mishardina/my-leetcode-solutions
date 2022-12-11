#https://leetcode.com/problems/valid-anagram

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {x:1 for x in s}
        t_dict = {x:1 for x in t}

        for i in range(0, len(s)):
            s_dict[s[i]] += 1
        for i in range(0, len(t)):
            t_dict[t[i]] += 1

        return s_dict.keys() == t_dict.keys() and s_dict.items() == t_dict.items()