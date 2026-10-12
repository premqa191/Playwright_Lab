class TreeNode:
    """బైనరీ ట్రీ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: TreeNode) -> int:
    """
    Time Complexity: O(N) - ట్రీలోని ప్రతి నోడ్‌ను ఒకేసారి సందర్శిస్తుంది.
    Space Complexity: O(H) - రికర్షన్ కాల్ స్టాక్ గరిష్టంగా ట్రీ ఎత్తు (Height) పరిమాణంలో ఉంటుంది.
    """
    # బేస్ కేస్: నోడ్ లేకపోతే లోతు 0
    if not root:
        return 0

    # ఎడమ మరియు కుడి సబ్‌ట్రీల డెప్త్‌ను లెక్కించడం
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)

    # గరిష్ట లోతుకు రూట్ నోడ్ (1) జోడించడం
    return 1 + max(left_depth, right_depth)

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక ట్రీ [3, 9, 20, None, None, 15, 7]
    #         3
    #        / \
    #       9   20
    #          /  \
    #         15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    assert max_depth(root1) == 3, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: కేవలం రూట్ నోడ్ మాత్రమే ఉన్నప్పుడు
    root2 = TreeNode(1)
    assert max_depth(root2) == 1, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: ఖాళీ ట్రీ (None)
    assert max_depth(None) == 0, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: స్కివ్డ్ ట్రీ (Skewed Tree - ఒకే వైపు పెరిగిన ట్రీ: 1 -> 2 -> 3)
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    root4.right.right = TreeNode(3)
    assert max_depth(root4) == 3, "Test case 4 failed"

    print("All Maximum Depth of Binary Tree assertions passed successfully with O(N) DFS!")