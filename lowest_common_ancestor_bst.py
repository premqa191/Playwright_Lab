class TreeNode:
    """బైనరీ ట్రీ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """
    Time Complexity: O(H) - గరిష్టంగా రూట్ నుండి లీఫ్ వరకు ఒకే ఒక మార్గంలో ప్రయాణిస్తుంది (Balanced BST లో O(log N)).
    Space Complexity: O(1) - రికర్షన్ స్టాక్ లేకుండా పాయింటర్ లూప్‌తో స్థిర మెమరీతో నడుస్తుంది.
    """
    curr = root

    while curr:
        # రెండూ చిన్నవైతే ఎడమ సబ్‌ట్రీకి వెళ్లడం
        if p.val < curr.val and q.val < curr.val:
            curr = curr.left
        # రెండూ పెద్దవైతే కుడి సబ్‌ట్రీకి వెళ్లడం
        elif p.val > curr.val and q.val > curr.val:
            curr = curr.right
        # స్ప్లిట్ పాయింట్ వచ్చినప్పుడు LCA దొరికినట్లే
        else:
            return curr

    return None

if __name__ == "__main__":
    # BST నిర్మాణం: [6, 2, 8, 0, 4, 7, 9, None, None, 3, 5]
    #         6
    #       /   \
    #      2     8
    #     / \   / \
    #    0   4 7   9
    #       / \
    #      3   5
    n0 = TreeNode(0)
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n4 = TreeNode(4, n3, n5)
    n2 = TreeNode(2, n0, n4)

    n7 = TreeNode(7)
    n9 = TreeNode(9)
    n8 = TreeNode(8, n7, n9)

    root = TreeNode(6, n2, n8)

    # టెస్ట్ కేస్ 1: p = 2, q = 8 (LCA = 6)
    lca1 = lowest_common_ancestor(root, n2, n8)
    assert lca1.val == 6, f"Test case 1 failed: Expected 6, got {lca1.val}"

    # టెస్ట్ కేస్ 2: p = 2, q = 4 (LCA = 2 - ఒక నోడ్ తనకు తానే పూర్వీకుడు)
    lca2 = lowest_common_ancestor(root, n2, n4)
    assert lca2.val == 2, f"Test case 2 failed: Expected 2, got {lca2.val}"

    # టెస్ట్ కేస్ 3: p = 3, q = 5 (LCA = 4)
    lca3 = lowest_common_ancestor(root, n3, n5)
    assert lca3.val == 4, f"Test case 3 failed: Expected 4, got {lca3.val}"

    # టెస్ట్ కేస్ 4: p = 7, q = 9 (LCA = 8)
    lca4 = lowest_common_ancestor(root, n7, n9)
    assert lca4.val == 8, f"Test case 4 failed: Expected 8, got {lca4.val}"

    # టెస్ట్ కేస్ 5: p = 3, q = 0 (LCA = 2)
    lca5 = lowest_common_ancestor(root, n3, n0)
    assert lca5.val == 2, f"Test case 5 failed: Expected 2, got {lca5.val}"

    print("All Lowest Common Ancestor (BST) assertions passed successfully with O(H) time and O(1) space complexity!")