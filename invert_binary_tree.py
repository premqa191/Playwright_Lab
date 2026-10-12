class TreeNode:
    """బైనరీ ట్రీ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def invert_tree(root: TreeNode) -> TreeNode:
    """
    Time Complexity: O(N) - ప్రతి నోడ్‌ను ఒకేసారి సందర్శించి స్వాప్ చేస్తుంది.
    Space Complexity: O(H) - రికర్షన్ కాల్ స్టాక్ ట్రీ ఎత్తుకు సమానమైన మెమరీని వాడుతుంది.
    """
    # బేస్ కేస్: నోడ్ లేకపోతే None రిటర్న్ చేయడం
    if not root:
        return None

    # ఎడమ మరియు కుడి పిల్లలను స్వాప్ చేయడం
    root.left, root.right = root.right, root.left

    # ఎడమ, కుడి సబ్‌ట్రీలకు రికర్సివ్‌గా అమలు చేయడం
    invert_tree(root.left)
    invert_tree(root.right)

    return root

# టెస్టింగ్ కోసం లెవెల్ ఆర్డర్ జాబితాగా మార్చే సహాయక ఫంక్షన్
def tree_to_list(root: TreeNode) -> list:
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # చివర ఉన్న అనవసరమైన None విలువలను తొలగించడం
    while result and result[-1] is None:
        result.pop()
    return result

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక ట్రీ [4, 2, 7, 1, 3, 6, 9]
    #         4
    #       /   \
    #      2     7
    #     / \   / \
    #    1   3 6   9
    root1 = TreeNode(4)
    root1.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root1.right = TreeNode(7, TreeNode(6), TreeNode(9))

    inverted1 = invert_tree(root1)
    assert tree_to_list(inverted1) == [4, 7, 2, 9, 6, 3, 1], "Test case 1 failed"

    # టెస్ట్ కేస్ 2: కేవలం రెండు స్థాయిలు ఉన్న ట్రీ [2, 1, 3] -> [2, 3, 1]
    root2 = TreeNode(2, TreeNode(1), TreeNode(3))
    inverted2 = invert_tree(root2)
    assert tree_to_list(inverted2) == [2, 3, 1], "Test case 2 failed"

    # టెస్ట్ కేస్ 3: ఖాళీ ట్రీ
    assert invert_tree(None) is None, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఒకే ఒక నోడ్ ఉన్న ట్రీ
    root4 = TreeNode(1)
    assert tree_to_list(invert_tree(root4)) == [1], "Test case 4 failed"

    print("All Invert Binary Tree assertions passed successfully with O(N) DFS!")