def search_rotated(nums: list[int], target: int) -> int:
    """
    Time Complexity: O(log N) - సార్టెడ్ అర్ధభాగాన్ని గుర్తిస్తూ సెర్చ్ స్పేస్‌ను సగానికి తగ్గిస్తుంది.
    Space Complexity: O(1) - అదనపు డేటా స్ట్రక్చర్స్ లేకుండా స్థిర మెమరీతో నడుస్తుంది.
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            return mid

        # ఎడమ అర్ధభాగం సార్ట్ అయి ఉందో లేదో తనిఖీ చేయడం
        if nums[left] <= nums[mid]:
            # టార్గెట్ ఎడమ భాగంలోనే ఉంటే
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # లేదంటే కుడి అర్ధభాగం ఖచ్చితంగా సార్ట్ అయి ఉంటుంది
        else:
            # టార్గెట్ కుడి భాగంలోనే ఉంటే
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: పివొట్ కుడివైపు టార్గెట్ ఉన్నప్పుడు
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 0) == 4, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: లిస్ట్‌లో లేని సంఖ్య
    assert search_rotated([4, 5, 6, 7, 0, 1, 2], 3) == -1, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: ఒకే ఎలిమెంట్ ఉండి మ్యాచ్ కానప్పుడు
    assert search_rotated([1], 0) == -1, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఒకే ఎలిమెంట్ ఉండి మ్యాచ్ అయినప్పుడు
    assert search_rotated([1], 1) == 0, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: పివొట్ ఎడమవైపు టార్గెట్ ఉన్నప్పుడు
    assert search_rotated([6, 7, 1, 2, 3, 4, 5], 7) == 1, "Test case 5 failed"

    # టెస్ట్ కేస్ 6: రెండు ఎలిమెంట్లు రొటేట్ అయినప్పుడు
    assert search_rotated([3, 1], 1) == 1, "Test case 6 failed"

    print("All Search in Rotated Sorted Array assertions passed successfully with O(log N) complexity!")