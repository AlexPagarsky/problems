import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        _map = collections.defaultdict(list)
        queue = [(root, 0)]

        while queue:
            report = []
            rmap = collections.defaultdict(list)

            for node, x in queue:
                rmap[x].append(node.val)

                if node.left:
                    report += (node.left, x - 1),
                if node.right:
                    report += (node.right, x + 1),

            for i in rmap:
                _map[i] += sorted(rmap[i])

            queue = report
        print(_map.items())
        return [_map[i] for i in sorted(_map)]