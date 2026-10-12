def two_sum_sorted(numbers: list[int], target: int) -> list[int]:
    """
    Time Complexity: O(N) - సార్టెడ్ లిస్ట్‌ను రెండు వైపుల నుండి ఒకేసారి స్కాన్ చేస్తుంది.
    Space Complexity: O(1) - అదనపు డిక్షనరీ లేదా డేటా స్ట్రక్చర్స్ లేకుండా పాయింటర్లతోనే పనిచేస్తుంది.
    """
    left = 0
    right = len(numbers) - 1

    while left < right:
        current_sum = numbers[left] + numbers[right]

        if current_sum == target:
            # ప్రశ్న నిబంధన ప్రకారం 1-based index రిటర్న్ చేయాలి
            return [left + 1, right + 1]
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return []

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: సాధారణ సార్టెడ్ లిస్ట్
    assert two_sum_sorted([2, 7, 11, 15], 9) == [1, 2], "Test case 1 failed"

    # టెస్ట్ కేస్ 2: నెగటివ్ నంబర్లతో కూడిన సార్టెడ్ లిస్ట్
    assert two_sum_sorted([-1, 0], -1) == [1, 2], "Test case 2 failed"

    # టెస్ట్ కేస్ 3: డూప్లికేట్ సంఖ్యలు ఉన్న సార్టెడ్ లిస్ట్
    assert two_sum_sorted([2, 3, 4], 6) == [1, 3], "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఒకే విలువ ఉన్న జత
    assert two_sum_sorted([5, 25, 75], 100) == [2, 3], "Test case 4 failed"

    print("All Two Sum II (Sorted Array) assertions passed successfully with O(1) space complexity!")