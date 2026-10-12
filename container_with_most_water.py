def max_area(height: list[int]) -> int:
    """
    Time Complexity: O(N) - జాబితాను రెండు వైపుల నుండి ఒకే ఒక పాస్‌లో స్కాన్ చేస్తుంది.
    Space Complexity: O(1) - అదనపు డేటా స్ట్రక్చర్స్ లేకుండా స్థిరమైన మెమరీతో నడుస్తుంది.
    """
    left = 0
    right = len(height) - 1
    max_water = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_water = width * current_height
        
        # గరిష్ట నీటి నిల్వను అప్‌డేట్ చేయడం
        max_water = max(max_water, current_water)

        # పొట్టిగా ఉన్న వైపు పాయింటర్‌ను మాత్రమే ముందుకు జరపడం
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక అసెస్‌మెంట్ కేస్ (గరిష్ట ఏరియా: 7 * 7 = 49)
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: కేవలం రెండు సమాన ఎత్తులు ఉన్న కేస్ (1 * 1 = 1)
    assert max_area([1, 1]) == 1, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: తగ్గుతున్న క్రమంలో ఉన్న ఎత్తులు
    assert max_area([4, 3, 2, 1, 4]) == 16, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: మధ్యలో పెద్ద గోడలు ఉన్న కేస్
    assert max_area([1, 2, 1]) == 2, "Test case 4 failed"

    print("All Container With Most Water assertions passed successfully with O(N) time and O(1) space complexity!")