def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Time Complexity: O(N) - ఒకే ఒక పాస్‌లో లిస్ట్‌ను స్కాన్ చేస్తుంది.
    Space Complexity: O(N) - సంఖ్యలు, వాటి ఇండెక్స్‌లను భద్రపరచడానికి డిక్షనరీని వాడుతుంది.
    """
    seen = {}  # {సంఖ్య: ఇండెక్స్}

    for current_index, num in enumerate(nums):
        complement = target - num
        
        # కాంప్లిమెంట్ డిక్షనరీలో ఉందో లేదో O(1) సమయంలో తనిఖీ చేస్తుంది
        if complement in seen:
            return [seen[complement], current_index]
        
        # ప్రస్తుత సంఖ్యను మరియు దాని ఇండెక్స్‌ను డిక్షనరీలో స్టోర్ చేస్తుంది
        seen[num] = current_index

    return []

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక కేస్
    nums_1 = [2, 7, 11, 15]
    target_1 = 9
    assert two_sum(nums_1, target_1) == [0, 1], "Test case 1 failed"

    # టెస్ట్ కేస్ 2: నెగటివ్ నంబర్లతో కూడిన కేస్
    nums_2 = [-3, 4, 3, 90]
    target_2 = 0
    assert two_sum(nums_2, target_2) == [0, 2], "Test case 2 failed"

    # టెస్ట్ కేస్ 3: సమాన సంఖ్యలు ఉన్న కేస్
    nums_3 = [3, 3]
    target_3 = 6
    assert two_sum(nums_3, target_3) == [0, 1], "Test case 3 failed"

    print("All Two Sum assertions passed successfully with O(N) time complexity!")