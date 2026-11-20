def length_of_lis(nums: list[int]) -> int:
    """
    Time Complexity: O(N^2) - నెస్టెడ్ లూప్స్ ద్వారా ప్రతి ఎలిమెంట్‌ను దాని మునుపటి ఎలిమెంట్స్‌తో పోలుస్తాం.
    Space Complexity: O(N) - N పరిమాణం గల DP అర్రేని ఉపయోగిస్తాం.
    """
    if not nums:
        return 0

    n = len(nums)
    # ప్రతి ఎలిమెంట్ కనీసం 1 పొడవు గల సబ్‌సీక్వెన్స్ అవుతుంది
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], 1 + dp[j])

    return max(dp)

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక కేస్ (ఉదాహరణ: [2, 3, 7, 101] -> పొడవు 4)
    assert length_of_lis([10, 9, 2, 5, 3, 7, 101, 18]) == 4, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: పునరావృత మూలకాలతో కూడిన కేస్
    assert length_of_lis([0, 1, 0, 3, 2, 3]) == 4, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: అన్ని సమాన సంఖ్యలు ఉన్నప్పుడు
    assert length_of_lis([7, 7, 7, 7, 7, 7, 7]) == 1, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: కేవలం ఒకే ఒక సంఖ్య ఉన్నప్పుడు
    assert length_of_lis([1]) == 1, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: ఇప్పటికే క్రమబద్ధీకరించబడిన జాబితా
    assert length_of_lis([1, 2, 3, 4, 5]) == 5, "Test case 5 failed"

    # టెస్ట్ కేస్ 6: అవరోహణ క్రమంలో ఉన్న జాబితా
    assert length_of_lis([5, 4, 3, 2, 1]) == 1, "Test case 6 failed"

    print("All Longest Increasing Subsequence assertions passed successfully with O(N^2) DP!")