#  https://leetcode.com/explore/featured/card/top-interview-questions-easy/102/math/878/


class Solution:
    def romanToInt(self, s: 'str') -> 'int':
        dict_ = {
                   'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
                   }
        result, i = 0, 0
        while i < len(s):
                try:
                    result += dict_[s[i] + s[i + 1]]
                    i += 2
                except (KeyError, IndexError):
                    result += dict_[s[i]]
                    i += 1
        return result