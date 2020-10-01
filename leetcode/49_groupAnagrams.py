class Solution:
    def groupAnagrams(self, strs):
        # ans = {}
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return ans.values()


        # res = {}

        # for s in strs:
        #     s = str(sorted(s))
        #     if res.setdefault(s, default=[]):
        #         res[s].append(s)

        # return [x for x in res.values()]
