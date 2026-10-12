class TreeNode:
    """బైనరీ ట్రీ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def good_nodes(root: TreeNode) -> int:
    """
    Time Complexity: O(N) - ట్రీలోని ప్రతి నోడ్‌ను ఒక్కసారి మాత్రమే సందర్శిస్తుంది.
    Space Complexity: O(H) - రికర్షన్ కాల్ స్టాక్ ట్రీ ఎత్తుకు పరిమితం.
    """
    def dfs(node: TreeNode, max_val: int) -> int:
        if not node:
            return 0

        # ప్రస్తుత నోడ్ విలువ మార్గంలోని గరిష్ట విలువ కంటే పెద్దదైనా/సమానమైనా గుడ్ నోడ్
        is_good = 1 if node.val >= max_val else 0
        current_max = max(max_val, node.val)

        # ఎడమ మరియు కుడి సబ్‌ట్రీలలో గుడ్ నోడ్లను లెక్కింపు
        return is_good + dfs(node.left, current_max) + dfs(node.right, current_max)

    if not root:
        return 0

    return dfs(root, root.val)

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక ట్రీ [3, 1, 4, 3, None, 1, 5] -> ఫలితం: 4
    #         3*
    #       /   \
    #      1     4*
    #     /     /  \
    #    3*    1    5*
    root1 = TreeNode(3)
    root1.left = TreeNode(1, TreeNode(3), None)
    root1.right = TreeNode(4, TreeNode(1), TreeNode(5))
    assert good_nodes(root1) == 4, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: ఆరోహణ క్రమంలో విలువలు పెరుగుతున్న ట్రీ [1, 2, 3] -> అన్నీ గుడ్ నోడ్లే (3)
    #       1*
    #        \
    #         2*
    #          \
    #           3*
    root2 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert good_nodes(root2) == 3, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: అవరోహణ క్రమంలో విలువలు తగ్గుతున్న ట్రీ [3, 2, 1] -> రూట్ మాత్రమే గుడ్ నోడ్ (1)
    #       3*
    #      /
    #     2
    #    /
    #   1
    root3 = TreeNode(3, TreeNode(2, TreeNode(1), None), None)
    assert good_nodes(root3) == 1, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఒకే విలువ కలిగిన అన్ని నోడ్స్ [3, 3, 3] -> అన్నీ సమానం కాబట్టి గుడ్ నోడ్లే (3)
    root4 = TreeNode(3, TreeNode(3), TreeNode(3))
    assert good_nodes(root4) == 3, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: ఒకే రూట్ నోడ్ ఉన్నప్పుడు
    assert good_nodes(TreeNode(10)) == 1, "Test case 5 failed"

    print("All Count Good Nodes in Binary Tree assertions passed successfully with O(N) DFS!")