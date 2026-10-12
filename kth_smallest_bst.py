class TreeNode:
    """బైనరీ ట్రీ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root: TreeNode, k: int) -> int:
    """
    Time Complexity: O(H + k) - ఎడమవైపు లీఫ్ వరకు వెళ్లి, k ఎలిమెంట్లను ప్రాసెస్ చేసిన వెంటనే ఆగిపోతుంది.
    Space Complexity: O(H) - స్టాక్ గరిష్టంగా ట్రీ ఎత్తు (Height) పరిమాణంలో ఉంటుంది.
    """
    stack = []
    curr = root

    while curr or stack:
        # ఎడమవైపు ఉన్న అత్యల్ప నోడ్ వరకు స్టాక్‌లో భద్రపరచడం
        while curr:
            stack.append(curr)
            curr = curr.left

        # అతి చిన్న విలువ కలిగిన నోడ్‌ను బయటకు తీయడం
        curr = stack.pop()
        k -= 1

        # k-వ మూలకం దొరికిన వెంటనే రిటర్న్ చేయడం
        if k == 0:
            return curr.val

        # కుడి సబ్‌ట్రీ వైపు అడుగు వేయడం
        curr = curr.right

    return -1

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ట్రీ [3, 1, 4, None, 2]
    #         3
    #        / \
    #       1   4
    #        \
    #         2
    root1 = TreeNode(3)
    root1.left = TreeNode(1, None, TreeNode(2))
    root1.right = TreeNode(4)

    assert kth_smallest(root1, 1) == 1, "Test case 1 failed: Expected 1"
    assert kth_smallest(root1, 2) == 2, "Test case 1 failed: Expected 2"
    assert kth_smallest(root1, 3) == 3, "Test case 1 failed: Expected 3"
    assert kth_smallest(root1, 4) == 4, "Test case 1 failed: Expected 4"

    # టెస్ట్ కేస్ 2: పెద్ద ట్రీ [5, 3, 6, 2, 4, None, None, 1]
    #           5
    #          / \
    #         3   6
    #        / \
    #       2   4
    #      /
    #     1
    root2 = TreeNode(5)
    root2.left = TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4))
    root2.right = TreeNode(6)

    assert kth_smallest(root2, 3) == 3, "Test case 2 failed: Expected 3"
    assert kth_smallest(root2, 1) == 1, "Test case 2 failed: Expected 1"
    assert kth_smallest(root2, 6) == 6, "Test case 2 failed: Expected 6"

    # టెస్ట్ కేస్ 3: ఒకే రూట్ నోడ్ ఉన్నప్పుడు
    root3 = TreeNode(10)
    assert kth_smallest(root3, 1) == 10, "Test case 3 failed"

    print("All Kth Smallest Element in a BST assertions passed successfully with O(H + k) time and O(H) space complexity!")