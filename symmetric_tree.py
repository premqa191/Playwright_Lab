class TreeNode:
    """బైనరీ ట్రీ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root: TreeNode) -> bool:
    """
    Time Complexity: O(N) - ట్రీలోని ప్రతి నోడ్‌ను ఒక్కసారి మాత్రమే సందర్శిస్తుంది.
    Space Complexity: O(H) - రికర్షన్ కాల్ స్టాక్ ట్రీ ఎత్తుకు సమానమైన మెమరీని వాడుతుంది.
    """
    if not root:
        return True

    def is_mirror(t1: TreeNode, t2: TreeNode) -> bool:
        # రెండూ శూన్యమైతే సమరూపం
        if not t1 and not t2:
            return True
        # ఏదో ఒకటి మాత్రమే శూన్యమైతే లేదా విలువలు సరిపోలకపోతే అసమరూపం
        if not t1 or not t2 or t1.val != t2.val:
            return False

        # మిర్రర్ కండిషన్: t1 ఎడమ vs t2 కుడి, మరియు t1 కుడి vs t2 ఎడమ
        return is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)

    return is_mirror(root.left, root.right)

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: సంపూర్ణ సమరూప ట్రీ [1, 2, 2, 3, 4, 4, 3]
    #         1
    #       /   \
    #      2     2
    #     / \   / \
    #    3   4 4   3
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(3), TreeNode(4))
    root1.right = TreeNode(2, TreeNode(4), TreeNode(3))
    assert is_symmetric(root1) is True, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: అసమరూప ట్రీ [1, 2, 2, None, 3, None, 3]
    #         1
    #       /   \
    #      2     2
    #       \     \
    #        3     3
    root2 = TreeNode(1)
    root2.left = TreeNode(2, None, TreeNode(3))
    root2.right = TreeNode(2, None, TreeNode(3))
    assert is_symmetric(root2) is False, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: ఒకే రూట్ నోడ్ ఉన్న ట్రీ
    root3 = TreeNode(1)
    assert is_symmetric(root3) is True, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఖాళీ ట్రీ (None)
    assert is_symmetric(None) is True, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: విలువలు సరిపోలని సమరూప నిర్మాణం
    root5 = TreeNode(1)
    root5.left = TreeNode(2, TreeNode(3), None)
    root5.right = TreeNode(2, TreeNode(3), None)
    assert is_symmetric(root5) is False, "Test case 5 failed"

    print("All Symmetric Tree assertions passed successfully with O(N) DFS!")