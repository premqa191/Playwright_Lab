def first_uniq_char(s: str) -> int:
    """
    Time Complexity: O(N) - స్ట్రింగ్‌ను రెండుసార్లు మాత్రమే స్కాన్ చేస్తుంది.
    Space Complexity: O(1) - ఇంగ్లీష్ ఆల్ఫాబెట్స్ గరిష్టంగా 26 అక్షరాలు మాత్రమే ఉంటాయి కాబట్టి స్థిరమైన మెమరీ.
    """
    char_counts = {}

    # పాస్ 1: ప్రతి అక్షరం యొక్క ఫ్రీక్వెన్సీని లెక్కించడం
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # పాస్ 2: మొదటి నాన్-రిపీటింగ్ అక్షరం ఇండెక్స్‌ను గుర్తించడం
    for index, char in enumerate(s):
        if char_counts[char] == 1:
            return index

    return -1

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: మొదటి అక్షరమే నాన్-రిపీటింగ్ అయినప్పుడు
    assert first_uniq_char("leetcode") == 0, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: మధ్యలో ఉన్న అక్షరం యునిక్ అయినప్పుడు
    assert first_uniq_char("loveleetcode") == 2, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: అన్ని అక్షరాలూ రిపీట్ అయినప్పుడు
    assert first_uniq_char("aabb") == -1, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఒకే అక్షరం ఉన్నప్పుడు
    assert first_uniq_char("z") == 0, "Test case 4 failed"

    print("All First Unique Character assertions passed successfully with O(N) time complexity!")