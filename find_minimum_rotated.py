def find_min(nums: list[int]) -> int:
    """
    Time Complexity: O(log N) - ప్రతి లూప్‌లోనూ సెర్చ్ స్పేస్‌ను సగానికి తగ్గిస్తుంది.
    Space Complexity: O(1) - స్థిరమైన మెమరీతో ఇన్-ప్లేస్ పరిశీలన చేస్తుంది.
    """
    left = 0
    right = len(nums) - 1

    # జాబితా ఇప్పటికే పూర్తిగా సార్ట్ అయి ఉంటే (రొటేషన్ పూర్తి చక్రం అయినప్పుడు)
    if nums[left] <= nums[right]:
        return nums[left]

    while left < right:
        mid = left + (right - left) // 2

        # మిడ్ విలువ కుడి చివర కంటే పెద్దదైతే, కనిష్ట సంఖ్య కుడి అర్ధభాగంలో ఉంది
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            # మిడ్ విలువ కనిష్ట సంఖ్య కావచ్చు లేదా దానికి ఎడమవైపు ఉండవచ్చు
            right = mid

    return nums[left]

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక రొటేటెడ్ అర్రే
    assert find_min([3, 4, 5, 1, 2]) == 1, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: పివొట్ మధ్యలో ఉన్నప్పుడు
    assert find_min([4, 5, 6, 7, 0, 1, 2]) == 0, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: రొటేట్ కాని క్రమబద్ధీకరించిన జాబితా
    assert find_min([11, 13, 15, 17]) == 11, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: కేవలం రెండు మూలకాలు మాత్రమే ఉన్నప్పుడు
    assert find_min([2, 1]) == 1, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: ఒకే ఒక మూలకం ఉన్నప్పుడు
    assert find_min([10]) == 10, "Test case 5 failed"

    # టెస్ట్ కేస్ 6: చివరి మూలకం మాత్రమే కనిష్టమైనప్పుడు
    assert find_min([2, 3, 4, 5, 1]) == 1, "Test case 6 failed"

    print("All Find Minimum in Rotated Sorted Array assertions passed successfully with O(log N) complexity!")