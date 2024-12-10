class Solution:
    def maximumLength(self, s: str) -> int:
        d = defaultdict(int)
        ans = -1
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if s[j-1] != s[i]:
                    break
                else:
                    d[s[i:j]] += 1
                if d[s[i:j]] >= 3:
                    ans = max(ans, j-i)
        return ans
