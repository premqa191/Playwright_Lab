from collections import deque

class TreeNode:
    """బైనరీ ట్రీ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, left: "TreeNode" = None, right: "TreeNode" = None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: TreeNode) -> list[list[int]]:
    """
    Time Complexity: O(N) - ట్రీలోని ప్రతి నోడ్‌ను ఖచ్చితంగా ఒకేసారి సందర్శిస్తుంది.
    Space Complexity: O(N) - క్యూ గరిష్టంగా ట్రీ యొక్క అత్యధిక వెడల్పు (గరిష్టంగా N/2 నోడ్స్) ఉన్న స్థాయిని భద్రపరుస్తుంది.
    """
    if not root:
        return []

    result = []
    queue = deque([root])

    while queue:
        level_size = len(queue)
        current_level = []

        # ప్రస్తుత స్థాయిలో ఉన్న నోడ్స్‌ను మాత్రమే ప్రాసెస్ చేయడం
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)

            # తదుపరి స్థాయి కోసం పిల్లలను క్యూలో చేర్చడం
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(current_level)

    return result

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక ట్రీ [3, 9, 20, None, None, 15, 7]
    #         3
    #        / \
    #       9   20
    #          /  \
    #         15   7
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
    assert level_order(root1) == [[3], [9, 20], [15, 7]], "Test case 1 failed"

    # టెస్ట్ కేస్ 2: కేవలం ఒకే రూట్ నోడ్ ఉన్నప్పుడు
    root2 = TreeNode(1)
    assert level_order(root2) == [[1]], "Test case 2 failed"

    # టెస్ట్ కేస్ 3: ఖాళీ ట్రీ (None)
    assert level_order(None) == [], "Test case 3 failed"

    # టెస్ట్ కేస్ 4: స్కివ్డ్ ట్రీ (Skewed Tree - 1 -> 2 -> 3)
    root4 = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert level_order(root4) == [[1], [2], [3]], "Test case 4 failed"

    # టెస్ట్ కేస్ 5: పూర్తి సంపూర్ణ బైనరీ ట్రీ
    #         1
    #       /   \
    #      2     3
    #     / \   / \
    #    4   5 6   7
    root5 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
    assert level_order(root5) == [[1], [2, 3], [4, 5, 6, 7]], "Test case 5 failed"

    print("All Binary Tree Level Order Traversal assertions passed successfully with O(N) BFS!")