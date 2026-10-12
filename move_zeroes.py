def move_zeroes(nums: list[int]) -> None:
    """
    Time Complexity: O(N) - జాబితాను ఒకేసారి స్కాన్ చేస్తుంది.
    Space Complexity: O(1) - ఉన్న జాబితాలోనే ఇన్-ప్లేస్ మార్పిడి చేస్తుంది (No extra memory).
    Do not return anything, modify nums in-place instead.
    """
    slow = 0

    for fast in range(len(nums)):
        if nums[fast] != 0:
            # నాన్-జీరో సంఖ్య కనిపించినప్పుడు స్వాప్ చేయడం
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక అర్రే
    test_1 = [0, 1, 0, 3, 12]
    move_zeroes(test_1)
    assert test_1 == [1, 3, 12, 0, 0], f"Test 1 Failed: {test_1}"

    # టెస్ట్ కేస్ 2: కేవలం ఒకే సున్నా ఉన్నప్పుడు
    test_2 = [0]
    move_zeroes(test_2)
    assert test_2 == [0], f"Test 2 Failed: {test_2}"

    # టెస్ట్ కేస్ 3: సున్నాలు ఏవీ లేనప్పుడు
    test_3 = [1, 2, 3, 4]
    move_zeroes(test_3)
    assert test_3 == [1, 2, 3, 4], f"Test 3 Failed: {test_3}"

    # టెస్ట్ కేస్ 4: అన్నీ సున్నాలే ఉన్నప్పుడు
    test_4 = [0, 0, 0]
    move_zeroes(test_4)
    assert test_4 == [0, 0, 0], f"Test 4 Failed: {test_4}"

    # టెస్ట్ కేస్ 5: ప్రారంభంలోనే నాన్-జీరోలు ఉన్నప్పుడు
    test_5 = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    move_zeroes(test_5)
    assert test_5 == [4, 2, 4, 3, 5, 1, 0, 0, 0, 0], f"Test 5 Failed: {test_5}"

    print("All Move Zeroes assertions passed successfully with O(N) time and O(1) space complexity!")