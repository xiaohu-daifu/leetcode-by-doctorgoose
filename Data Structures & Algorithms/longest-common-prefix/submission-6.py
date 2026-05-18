class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        sol = ""
        for x in zip(*strs):
            if x.count(x[0]) == len(x):
                print(f"{x} is same among all")
                sol += x[0]
            else:
                return sol
        return sol

                