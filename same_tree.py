class TreeNode:
    """బైనరీ ట్రీ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """
    Time Complexity: O(N) - రెండు ట్రీలలోని నోడ్లను సమాంతరంగా ఒకేసారి సందర్శిస్తుంది.
    Space Complexity: O(H) - రికర్షన్ కాల్ స్టాక్ ట్రీ ఎత్తుకు (Height) పరిమితమై ఉంటుంది.
    """
    # రెండూ శూన్యమైతే సమానం
    if not p and not q:
        return True

    # ఏదో ఒకటి మాత్రమే శూన్యమైతే లేదా విలువలు సరిపోలకపోతే అసమానం
    if not p or not q or p.val != q.val:
        return False

    # ఎడమ మరియు కుడి సబ్‌ట్రీలు రెండూ ఒకేలా ఉండాలి
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: సంపూర్ణంగా సమానమైన ట్రీలు [1, 2, 3] మరియు [1, 2, 3]
    t1_p = TreeNode(1, TreeNode(2), TreeNode(3))
    t1_q = TreeNode(1, TreeNode(2), TreeNode(3))
    assert is_same_tree(t1_p, t1_q) is True, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: నిర్మాణం భిన్నంగా ఉన్న కేస్
    # Tree 1: 1 -> left: 2
    # Tree 2: 1 -> right: 2
    t2_p = TreeNode(1, TreeNode(2), None)
    t2_q = TreeNode(1, None, TreeNode(2))
    assert is_same_tree(t2_p, t2_q) is False, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: నిర్మాణం సమానంగా ఉండి విలువలు మారిన కేస్
    t3_p = TreeNode(1, TreeNode(2), TreeNode(1))
    t3_q = TreeNode(1, TreeNode(1), TreeNode(2))
    assert is_same_tree(t3_p, t3_q) is False, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: రెండూ ఖాళీ ట్రీలు (None, None)
    assert is_same_tree(None, None) is True, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: ఒకటి ఖాళీగా, మరొకటి విలువతో ఉన్నప్పుడు
    assert is_same_tree(TreeNode(1), None) is False, "Test case 5 failed"

    print("All Same Tree assertions passed successfully with O(N) DFS!")