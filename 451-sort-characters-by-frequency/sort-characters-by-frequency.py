from collections import Counter

class Solution(object):
    def frequencySort(self, s):
        freq = Counter(s)
        ans = ""

        for ch, count in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            ans += ch * count

        return ans