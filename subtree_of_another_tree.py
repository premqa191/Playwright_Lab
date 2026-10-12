class TreeNode:
    """బైనరీ ట్రీ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p: TreeNode, q: TreeNode) -> bool:
    """రెండు ట్రీల నిర్మాణం మరియు విలువలు సమానమా కాదా అని పరీక్షిస్తుంది"""
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

def is_subtree(root: TreeNode, subRoot: TreeNode) -> bool:
    """
    Time Complexity: O(M * N) - ప్రధాన ట్రీలోని ప్రతి నోడ్ వద్ద subRoot సరిపోలికను తనిఖీ చేస్తుంది.
    Space Complexity: O(H) - రికర్షన్ కాల్ స్టాక్ ప్రధాన ట్రీ ఎత్తుకు సమానంగా ఉంటుంది.
    """
    if not subRoot:
        return True
    if not root:
        return False

    # ప్రస్తుత నోడ్ వద్ద రెండు ట్రీలు సమానమైతే True
    if is_same_tree(root, subRoot):
        return True

    # ఎడమ సబ్‌ట్రీలో గానీ, కుడి సబ్‌ట్రీలో గానీ సరిపోలిక ఉందో లేదో శోధించడం
    return is_subtree(root.left, subRoot) or is_subtree(root.right, subRoot)

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: సంపూర్ణ సబ్‌ట్రీ ఉన్న కేస్
    # Root Tree:
    #         3
    #        / \
    #       4   5
    #      / \
    #     1   2
    root1 = TreeNode(3)
    root1.left = TreeNode(4, TreeNode(1), TreeNode(2))
    root1.right = TreeNode(5)

    # Sub Tree:
    #       4
    #      / \
    #     1   2
    sub1 = TreeNode(4, TreeNode(1), TreeNode(2))
    assert is_subtree(root1, sub1) is True, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: అదనపు నోడ్స్ ఉన్నందున మ్యాచ్ కాని కేస్
    # Root Tree: 2 కింద అదనంగా 0 ఉంది
    root2 = TreeNode(3)
    root2.left = TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0), None))
    root2.right = TreeNode(5)
    assert is_subtree(root2, sub1) is False, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: రెండు ట్రీలు సరిగ్గా ఒకేలా ఉన్నప్పుడు
    single_root = TreeNode(1, TreeNode(2), None)
    single_sub = TreeNode(1, TreeNode(2), None)
    assert is_subtree(single_root, single_sub) is True, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: విలువలు సమానమైనా ఆకారం మారినప్పుడు
    t_root = TreeNode(1, TreeNode(1), None)
    t_sub = TreeNode(1, None, TreeNode(1))
    assert is_subtree(t_root, t_sub) is False, "Test case 4 failed"

    print("All Subtree of Another Tree assertions passed successfully with O(M * N) DFS!")