class TreeNode:
    """బైనరీ ట్రీ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root: TreeNode) -> int:
    """
    Time Complexity: O(N) - ప్రతి నోడ్‌ను ఖచ్చితంగా ఒకేసారి సందర్శిస్తుంది.
    Space Complexity: O(H) - రికర్షన్ కాల్ స్టాక్ ట్రీ ఎత్తుకు పరిమితం.
    """
    max_sum = float('-inf')

    def max_gain(node: TreeNode) -> int:
        nonlocal max_sum
        if not node:
            return 0

        # రుణాత్మక విలువలను నివారించడానికి max(0, gain) వాడటం
        left_gain = max(0, max_gain(node.left))
        right_gain = max(0, max_gain(node.right))

        # ప్రస్తుత నోడ్ వద్ద రెండు వైపులా కలిపి వచ్చే గరిష్ట మార్గాన్ని అంచనా వేయడం
        current_path_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, current_path_sum)

        # పేరెంట్ నోడ్ కోసం ఒకే ఒక అత్యుత్తమ బ్రాంచ్‌ను రిటర్న్ చేయడం
        return node.val + max(left_gain, right_gain)

    max_gain(root)
    return max_sum

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక పాజిటివ్ ట్రీ [1, 2, 3] -> మార్గం: 2 -> 1 -> 3 (మొత్తం = 6)
    #       1
    #      / \
    #     2   3
    root1 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert max_path_sum(root1) == 6, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: నెగటివ్ రూట్ మరియు పాజిటివ్ సబ్‌ట్రీలు [-10, 9, 20, None, None, 15, 7] -> 42
    #         -10
    #         /  \
    #        9    20
    #            /  \
    #           15   7
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert max_path_sum(root2) == 42, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: అన్ని నోడ్లూ నెగటివ్ విలువలే ఉన్నప్పుడు [-3] -> గరిష్టం -3 మాత్రమే
    root3 = TreeNode(-3)
    assert max_path_sum(root3) == -3, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: నెగటివ్ సంఖ్యలతో కూడిన పెద్ద ట్రీ [-2, -1] -> -1
    root4 = TreeNode(-2, TreeNode(-1), None)
    assert max_path_sum(root4) == -1, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: రూట్ కంటే సబ్‌ట్రీ మార్గమే భారీగా ఉన్నప్పుడు [2, -1] -> 2
    root5 = TreeNode(2, TreeNode(-1), None)
    assert max_path_sum(root5) == 2, "Test case 5 failed"

    print("All Binary Tree Maximum Path Sum assertions passed successfully with O(N) Post-Order DFS!")