class TreeNode:
    """బైనరీ ట్రీ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(root: TreeNode) -> bool:
    """
    Time Complexity: O(N) - ప్రతి నోడ్‌ను ఖచ్చితంగా ఒకేసారి సందర్శిస్తుంది.
    Space Complexity: O(H) - రికర్షన్ కాల్ స్టాక్ ట్రీ ఎత్తుకు సమానమైన మెమరీని వాడుతుంది.
    """
    def validate(node: TreeNode, low: float, high: float) -> bool:
        # ఖాళీ నోడ్ అయితే చెల్లుబాటు అవుతుంది
        if not node:
            return True

        # విలువ నిర్దేశిత పరిధిలో లేకపోతే BST కాదు
        if not (low < node.val < high):
            return False

        # ఎడమ సబ్‌ట్రీకి high = node.val, కుడి సబ్‌ట్రీకి low = node.val గా పరిధులు మార్చడం
        return validate(node.left, low, node.val) and validate(node.right, node.val, high)

    return validate(root, float('-inf'), float('inf'))

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: సరైన BST [2, 1, 3]
    #       2
    #      / \
    #     1   3
    root1 = TreeNode(2, TreeNode(1), TreeNode(3))
    assert is_valid_bst(root1) is True, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: చెల్లని BST [5, 1, 4, None, None, 3, 6]
    #         5
    #        / \
    #       1   4
    #          / \
    #         3   6
    # (ఇక్కడ రూట్ 5 కంటే కుడివైపు ఉన్న 4 చిన్నది కాబట్టి చెల్లదు)
    root2 = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    assert is_valid_bst(root2) is False, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: తీవ్రమైన అంచు కేస్ - స్థానికంగా సరైనదే అయినా గ్లోబల్ BST రూల్ ఉల్లంఘన
    #         5
    #        / \
    #       4   6
    #          / \
    #         3   7
    # (ఇక్కడ 3 అనేది 6 కి ఎడమవైపున ఉంది కాబట్టి లోకల్ గా కరెక్ట్, కానీ రూట్ 5 కంటే కుడివైపు ఉండి చిన్నదైనందున చెల్లదు)
    root3 = TreeNode(5, TreeNode(4), TreeNode(6, TreeNode(3), TreeNode(7)))
    assert is_valid_bst(root3) is False, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఒకే రూట్ నోడ్ ఉన్న ట్రీ
    assert is_valid_bst(TreeNode(10)) is True, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: ఖాళీ ట్రీ
    assert is_valid_bst(None) is True, "Test case 5 failed"

    # టెస్ట్ కేస్ 6: సమాన విలువలు ఉన్నప్పుడు (BST లో డూప్లికేట్స్ అనుమతించబడవు)
    root6 = TreeNode(2, TreeNode(2), TreeNode(2))
    assert is_valid_bst(root6) is False, "Test case 6 failed"

    print("All Validate Binary Search Tree assertions passed successfully with O(N) DFS Range Check!")