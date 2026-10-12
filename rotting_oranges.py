from collections import deque

def oranges_rotting(grid: list[list[int]]) -> int:
    """
    Time Complexity: O(R * C) - ప్రతి సెల్‌ను క్యూ ద్వారా గరిష్టంగా ఒకేసారి ప్రాసెస్ చేస్తాం.
    Space Complexity: O(R * C) - క్యూలో గరిష్టంగా ఉండే నారింజల సంఖ్య.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh_count = 0

    # 1. అన్ని కుళ్ళిన నారింజలను క్యూలో వేయడం మరియు తాజా నారింజలను లెక్కించడం
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh_count += 1

    # తాజా నారింజలు లేకపోతే సమయం 0
    if fresh_count == 0:
        return 0

    minutes = 0
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # కిందికి, పైకి, కుడికి, ఎడమకు

    # 2. Multi-Source BFS (లెవల్ బై లెవల్ ప్రాసెసింగ్)
    while queue and fresh_count > 0:
        minutes += 1
        # ప్రస్తుత నిమిషంలో ఉన్న అన్ని కుళ్ళిన నారింజలను ఏకకాలంలో ప్రాసెస్ చేయడం
        for _ in range(len(queue)):
            curr_r, curr_c = queue.popleft()

            for dr, dc in directions:
                nr, nc = curr_r + dr, curr_c + dc

                # గ్రిడ్ హద్దుల్లో ఉండి తాజా నారింజ (1) అయితే
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # కుళ్ళిపోయేలా మార్చడం
                    fresh_count -= 1
                    queue.append((nr, nc))

    # ఇంకా ఏవైనా తాజా నారింజలు మిగిలి ఉంటే కుళ్ళడం అసాధ్యం (-1)
    return minutes if fresh_count == 0 else -1

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక కేస్ (4 నిమిషాల్లో అన్నీ కుళ్ళిపోతాయి)
    g1 = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]
    assert oranges_rotting(g1) == 4, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: ఒక నారింజను తాకడం అసాధ్యం (-1)
    g2 = [
        [2, 1, 1],
        [0, 1, 1],
        [1, 0, 1]
    ]
    assert oranges_rotting(g2) == -1, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: తాజా నారింజలు ఏవీ లేవు (0 నిమిషాలు)
    g3 = [
        [0, 2]
    ]
    assert oranges_rotting(g3) == 0, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఒకే తాజా నారింజ, కుళ్ళినది ఏదీ లేదు (-1)
    g4 = [[1]]
    assert oranges_rotting(g4) == -1, "Test case 4 failed"

    print("All Rotting Oranges assertions passed successfully with O(R * C) Multi-Source BFS!")