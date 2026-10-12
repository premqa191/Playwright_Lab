class TreeNode:
    """బైనరీ ట్రీ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def diameter_of_binary_tree(root: TreeNode) -> int:
    """
    Time Complexity: O(N) - ప్రతి నోడ్‌ను ఖచ్చితంగా ఒకేసారి సందర్శిస్తుంది.
    Space Complexity: O(H) - రికర్షన్ కాల్ స్టాక్ ట్రీ ఎత్తుకు పరిమితం.
    """
    max_diameter = 0

    def get_height(node: TreeNode) -> int:
        nonlocal max_diameter
        if not node:
            return 0

        # ఎడమ మరియు కుడి సబ్‌ట్రీల ఎత్తులను లెక్కింపు
        left_h = get_height(node.left)
        right_h = get_height(node.right)

        # ప్రస్తుత నోడ్ వద్ద గరిష్ట మార్గాన్ని పోల్చడం (edges = left_h + right_h)
        max_diameter = max(max_diameter, left_h + right_h)

        # పై స్థాయి నోడ్ కోసం ఎత్తును రిటర్న్ చేయడం
        return 1 + max(left_h, right_h)

    get_height(root)
    return max_diameter

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక ట్రీ [1, 2, 3, 4, 5] -> వ్యాసం 3 (మార్గం: 4 -> 2 -> 1 -> 3)
    #         1
    #        / \
    #       2   3
    #      / \
    #     4   5
    root1 = TreeNode(1)
    root1.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root1.right = TreeNode(3)
    assert diameter_of_binary_tree(root1) == 3, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: కేవలం రెండు నోడ్స్ ఉన్నప్పుడు [1, 2] -> వ్యాసం 1
    root2 = TreeNode(1, TreeNode(2), None)
    assert diameter_of_binary_tree(root2) == 1, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: రూట్ గుండా వెళ్ళని పొడవైన మార్గం ఉన్న ట్రీ
    #         1
    #        /
    #       2
    #      / \
    #     3   4
    #    /     \
    #   5       6
    # (ఇక్కడ మార్గం: 5 -> 3 -> 2 -> 4 -> 6, మొత్తం ఎడ్జ్‌లు = 4, రూట్ 1 ఈ మార్గంలో లేదు)
    root3 = TreeNode(1)
    n2 = TreeNode(2)
    n2.left = TreeNode(3, TreeNode(5), None)
    n2.right = TreeNode(4, None, TreeNode(6))
    root3.left = n2
    assert diameter_of_binary_tree(root3) == 4, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఒకే ఒక రూట్ నోడ్ ఉన్నప్పుడు (Edges = 0)
    assert diameter_of_binary_tree(TreeNode(1)) == 0, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: ఖాళీ ట్రీ
    assert diameter_of_binary_tree(None) == 0, "Test case 5 failed"

    print("All Diameter of Binary Tree assertions passed successfully with O(N) DFS!")