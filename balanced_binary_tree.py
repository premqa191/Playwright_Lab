class TreeNode:
    """బైనరీ ట్రీ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: TreeNode) -> bool:
    """
    Time Complexity: O(N) - ప్రతి నోడ్‌ను బాటమ్-అప్ పద్ధతిలో ఒక్కసారి మాత్రమే సందర్శిస్తుంది.
    Space Complexity: O(H) - రికర్షన్ కాల్ స్టాక్ ట్రీ ఎత్తుకు సమానంగా ఉంటుంది.
    """
    def check_height(node: TreeNode) -> int:
        if not node:
            return 0

        left_h = check_height(node.left)
        if left_h == -1:
            return -1

        right_h = check_height(node.right)
        if right_h == -1:
            return -1

        # ఎత్తుల వ్యత్యాసం 1 కంటే ఎక్కువైతే అసమతుల్యం (-1)
        if abs(left_h - right_h) > 1:
            return -1

        return 1 + max(left_h, right_h)

    return check_height(root) != -1

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: సమతుల్యమైన ట్రీ [3, 9, 20, None, None, 15, 7]
    #         3
    #        / \
    #       9   20
    #          /  \
    #         15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert is_balanced(root1) is True, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: అసమతుల్యమైన ట్రీ [1, 2, 2, 3, 3, None, None, 4, 4]
    #               1
    #              / \
    #             2   2
    #            / \
    #           3   3
    #          / \
    #         4   4
    root2 = TreeNode(1)
    n2_left = TreeNode(2)
    n2_right = TreeNode(2)
    n3_left = TreeNode(3, TreeNode(4), TreeNode(4))
    n3_right = TreeNode(3)
    n2_left.left = n3_left
    n2_left.right = n3_right
    root2.left = n2_left
    root2.right = n2_right
    assert is_balanced(root2) is False, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: ఖాళీ ట్రీ (None) ఎల్లప్పుడూ బ్యాలెన్స్‌డ్
    assert is_balanced(None) is True, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఒకే ఒక రూట్ నోడ్ ఉన్నప్పుడు
    assert is_balanced(TreeNode(10)) is True, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: స్కివ్డ్ ట్రీ 1 -> 2 -> 3 (అసమతుల్యం)
    root5 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert is_balanced(root5) is False, "Test case 5 failed"

    print("All Balanced Binary Tree assertions passed successfully with O(N) Bottom-Up DFS!")
    