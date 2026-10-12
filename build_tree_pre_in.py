class TreeNode:
    """బైనరీ ట్రీ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(preorder: list[int], inorder: list[int]) -> TreeNode:
    """
    Time Complexity: O(N) - ప్రతి నోడ్‌ను హ్యాష్ మ్యాప్ సహాయంతో O(1) లో కనుగొని ఒకేసారి నిర్మిస్తుంది.
    Space Complexity: O(N) - ఇండెక్స్ మ్యాపింగ్ డిక్షనరీ మరియు రికర్షన్ స్టాక్ కోసం.
    """
    inorder_map = {val: i for i, val in enumerate(inorder)}
    pre_idx = 0

    def helper(in_left: int, in_right: int) -> TreeNode:
        nonlocal pre_idx
        if in_left > in_right:
            return None

        # ప్రీ-ఆర్డర్ నుండి ప్రస్తుత రూట్ విలువను ఎంపిక చేయడం
        root_val = preorder[pre_idx]
        pre_idx += 1
        root = TreeNode(root_val)

        # ఇన్-ఆర్డర్ లో రూట్ స్థానాన్ని గుర్తించడం
        mid = inorder_map[root_val]

        # ఎడమ మరియు కుడి సబ్‌ట్రీల రికర్సివ్ నిర్మాణం
        root.left = helper(in_left, mid - 1)
        root.right = helper(mid + 1, in_right)

        return root

    return helper(0, len(inorder) - 1)

# ధృవీకరణ కోసం లెవెల్-ఆర్డర్ జాబితాగా మార్చే సహాయక ఫంక్షన్
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
    while result and result[-1] is None:
        result.pop()
    return result

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక ట్రీ [3, 9, 20, None, None, 15, 7]
    pre1 = [3, 9, 20, 15, 7]
    in1 = [9, 3, 15, 20, 7]
    built_root1 = build_tree(pre1, in1)
    assert tree_to_list(built_root1) == [3, 9, 20, None, None, 15, 7], "Test case 1 failed"

    # టెస్ట్ కేస్ 2: ఒకే నోడ్ ఉన్నప్పుడు
    pre2 = [-1]
    in2 = [-1]
    built_root2 = build_tree(pre2, in2)
    assert tree_to_list(built_root2) == [-1], "Test case 2 failed"

    # టెస్ట్ కేస్ 3: కేవలం ఎడమవైపు మాత్రమే విస్తరించిన ట్రీ (Skewed Left: 3 -> 2 -> 1)
    pre3 = [3, 2, 1]
    in3 = [1, 2, 3]
    built_root3 = build_tree(pre3, in3)
    assert tree_to_list(built_root3) == [3, 2, None, 1], "Test case 3 failed"

    # టెస్ట్ కేస్ 4: కేవలం కుడివైపు మాత్రమే విస్తరించిన ట్రీ (Skewed Right: 1 -> 2 -> 3)
    pre4 = [1, 2, 3]
    in4 = [1, 2, 3]
    built_root4 = build_tree(pre4, in4)
    assert tree_to_list(built_root4) == [1, None, 2, None, 3], "Test case 4 failed"

    print("All Construct Tree from Preorder & Inorder assertions passed successfully with O(N) complexity!")