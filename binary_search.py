def search(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(log N) - ప్రతి దశలోనూ సెర్చ్ స్పేస్‌ను సగానికి తగ్గిస్తుంది.
    Space Complexity: O(1) - కేవలం రెండు పాయింటర్లతో స్థిర మెమరీతో నడుస్తుంది.
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        # పూర్ణాంక ఓవర్‌ఫ్లో నివారించే మిడ్ పాయింట్ సూత్రం
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక సార్టెడ్ లిస్ట్
    nums1 = [-1, 0, 3, 5, 9, 12]
    assert search(nums1, 9) == 4, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: లిస్ట్‌లో లేని సంఖ్య
    nums2 = [-1, 0, 3, 5, 9, 12]
    assert search(nums2, 2) == -1, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: ఒకే ఎలిమెంట్ ఉండి మ్యాచ్ అయినప్పుడు
    assert search([5], 5) == 0, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఒకే ఎలిమెంట్ ఉండి మ్యాచ్ కానప్పుడు
    assert search([5], -5) == -1, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: మొదటి స్థానంలోనే టార్గెట్ ఉన్నప్పుడు
    assert search([1, 2, 3, 4, 5], 1) == 0, "Test case 5 failed"

    # టెస్ట్ కేస్ 6: చివరి స్థానంలో టార్గెట్ ఉన్నప్పుడు
    assert search([1, 2, 3, 4, 5], 5) == 4, "Test case 6 failed"

    print("All Binary Search assertions passed successfully with O(log N) time complexity!")