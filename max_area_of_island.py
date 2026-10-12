def max_area_of_island(grid: list[list[int]]) -> int:
    """
    Time Complexity: O(R * C) - ప్రతి సెల్ గరిష్టంగా ఒకేసారి ప్రాసెస్ చేయబడుతుంది.
    Space Complexity: O(R * C) - అత్యంత దారుణమైన సందర్భంలో రికర్శన్ స్టాక్ సైజు.
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    max_area = 0

    def dfs(r: int, c: int) -> int:
        # హద్దులు దాటినా లేదా నీరు (0) అయినా వైశాల్యం 0
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0:
            return 0

        # సెల్‌ను నీటిగా మార్చడం (In-Place Sinking)
        grid[r][c] = 0

        # ప్రస్తుత సెల్ (1) + 4 దిశల మొత్తం వైశాల్యం
        area = 1
        area += dfs(r + 1, c)  # Down
        area += dfs(r - 1, c)  # Up
        area += dfs(r, c + 1)  # Right
        area += dfs(r, c - 1)  # Left

        return area

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                current_island_area = dfs(r, c)
                max_area = max(max_area, current_island_area)

    return max_area

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక గ్రిడ్ (గరిష్ట వైశాల్యం 6)
    g1 = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    assert max_area_of_island(g1) == 6, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: ద్వీపాలు లేని ఖాళీ నీటి గ్రిడ్
    g2 = [
        [0,0,0,0,0],
        [0,0,0,0,0]
    ]
    assert max_area_of_island(g2) == 0, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: మొత్తం ఒకే పెద్ద ద్వీపం (వైశాల్యం 4)
    g3 = [
        [1,1],
        [1,1]
    ]
    assert max_area_of_island(g3) == 4, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఒకే ఒక సెల్ ఉన్న ద్వీపం
    g4 = [[1]]
    assert max_area_of_island(g4) == 1, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: ఖాళీ గ్రిడ్
    assert max_area_of_island([]) == 0, "Test case 5 failed"

    print("All Max Area of Island assertions passed successfully with O(R * C) DFS!")