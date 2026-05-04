class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = set(s)
        ts = set(t)
        if ss == ts:
            for i in ss:
                if s.count(i) != t.count(i):
                    return False
            return True
        return False