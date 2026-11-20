from collections import deque

class TreeNode:
    """బైనరీ ట్రీ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def right_side_view(root: TreeNode) -> list[int]:
    """
    Time Complexity: O(N) - ట్రీలోని ప్రతి నోడ్‌ను ఒక్కసారి మాత్రమే సందర్శిస్తుంది.
    Space Complexity: O(D) - క్యూ గరిష్టంగా ఒక స్థాయిలోని నోడ్లను మాత్రమే నిల్వ చేస్తుంది (O(N)).
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)

        for i in range(level_size):
            node = queue.popleft()

            # ప్రస్తుత స్థాయిలో కుడి చివరన ఉన్న నోడ్ అయితే ఫలితంలోకి చేర్చడం
            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక ట్రీ [1, 2, 3, None, 5, None, 4] -> [1, 3, 4]
    #         1
    #       /   \
    #      2     3
    #       \     \
    #        5     4
    root1 = TreeNode(1)
    root1.left = TreeNode(2, None, TreeNode(5))
    root1.right = TreeNode(3, None, TreeNode(4))
    assert right_side_view(root1) == [1, 3, 4], "Test case 1 failed"

    # టెస్ట్ కేస్ 2: ఎడమ సబ్‌ట్రీ ఎక్కువ లోతుగా ఉన్న కేస్ [1, 2, 3, 4] -> [1, 3, 4]
    #         1
    #       /   \
    #      2     3
    #     /
    #    4
    # (ఇక్కడ మూడవ లెవెల్‌లో కుడివైపు ఏమీ లేదు కాబట్టి ఎడమవైపు ఉన్న 4 కనిపిస్తుంది)
    root2 = TreeNode(1)
    root2.left = TreeNode(2, TreeNode(4), None)
    root2.right = TreeNode(3)
    assert right_side_view(root2) == [1, 3, 4], "Test case 2 failed"

    # టెస్ట్ కేస్ 3: కేవలం ఎడమవైపు మాత్రమే విస్తరించిన స్కివ్డ్ ట్రీ 1 -> 2 -> 3
    root3 = TreeNode(1, TreeNode(2, TreeNode(3), None), None)
    assert right_side_view(root3) == [1, 2, 3], "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఖాళీ ట్రీ (None)
    assert right_side_view(None) == [], "Test case 4 failed"

    # టెస్ట్ కేస్ 5: ఒకే రూట్ నోడ్ ఉన్నప్పుడు
    assert right_side_view(TreeNode(42)) == [42], "Test case 5 failed"

    print("All Binary Tree Right Side View assertions passed successfully with O(N) BFS!")