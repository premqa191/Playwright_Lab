def num_islands(grid: list[list[str]]) -> int:
    """
    Time Complexity: O(R * C)
    Space Complexity: O(R * C)
    """
    if not grid or not grid[0]:
        return 0

    rows, cols = len(grid), len(grid[0])
    islands_count = 0

    def dfs(r: int, c: int):
        # గ్రిడ్ హద్దులు దాటినా లేదా నీరు ('0') ఉన్నా ఆగిపోవడం
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == "0":
            return

        # ప్రస్తుత ల్యాండ్‌ను నీటిగా మార్చడం (In-Place Sinking)
        grid[r][c] = "0"

        # 4 దిశల్లో ప్రయాణించడం
        dfs(r + 1, c)  # Down
        dfs(r - 1, c)  # Up
        dfs(r, c + 1)  # Right
        dfs(r, c - 1)  # Left

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                islands_count += 1
                dfs(r, c)

    return islands_count

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ఒకే ద్వీపం
    g1 = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]
    assert num_islands(g1) == 1, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: మూడు వేర్వేరు ద్వీపాలు
    g2 = [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"]
    ]
    assert num_islands(g2) == 3, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: మొత్తం నీరు ఉన్నప్పుడు
    g3 = [
        ["0", "0", "0"],
        ["0", "0", "0"]
    ]
    assert num_islands(g3) == 0, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: 4 విడి ద్వీపాలు
    g4 = [
        ["1", "0", "1"],
        ["0", "0", "0"],
        ["1", "0", "1"]
    ]
    assert num_islands(g4) == 4, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: ఖాళీ గ్రిడ్
    assert num_islands([]) == 0, "Test case 5 failed"

    print("All Number of Islands assertions passed successfully with O(R * C) DFS!")