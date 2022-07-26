class Solution:
    def letter_to_int(self, letter):
        if   letter == 'I': return 1
        elif letter == 'V': return 5
        elif letter == 'X': return 10
        elif letter == 'L': return 50
        elif letter == 'C': return 100
        elif letter == 'D': return 500
        elif letter == 'M': return 1000

    def romanToInt(self, s):
        deg = list(map(self.letter_to_int, s))
        res = 0
        i = len(deg) - 1

        while i >= 0:
            if i == 0 or deg[i] <= deg[i - 1]:
                res += deg[i]
                i -= 1
            elif deg[i] > deg[i - 1]:
                res += deg[i] - deg[i - 1]
                i -= 2

        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.romanToInt("MCMXCIV"))
