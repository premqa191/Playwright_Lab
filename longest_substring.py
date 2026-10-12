def length_of_longest_substring(s: str) -> int:
    """
    Time Complexity: O(N) - స్ట్రింగ్‌ను కేవలం ఒకే ఒకసారి స్కాన్ చేస్తుంది.
    Space Complexity: O(min(N, M)) - అక్షరాల ఇండెక్స్‌లను స్టోర్ చేయడానికి డిక్షనరీని వాడుతుంది.
    """
    char_map = {}
    left = 0
    max_length = 0

    for right in range(len(s)):
        current_char = s[right]

        # అక్షరం ప్రస్తుత విండో లోపల రిపీట్ అయితే ఎడమ పాయింటర్‌ను ముందుకు జరపడం
        if current_char in char_map and char_map[current_char] >= left:
            left = char_map[current_char] + 1

        # అక్షరం యొక్క తాజా ఇండెక్స్‌ను సేవ్ చేయడం
        char_map[current_char] = right

        # గరిష్ట పొడవును అప్‌డేట్ చేయడం
        current_window_len = right - left + 1
        if current_window_len > max_length:
            max_length = current_window_len

    return max_length

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక కేస్ ("abc" -> 3)
    assert length_of_longest_substring("abcabcbb") == 3, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: ఒకే అక్షరం రిపీట్ అయిన కేస్ ("b" -> 1)
    assert length_of_longest_substring("bbbbb") == 1, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: మధ్యలో సబ్‌స్ట్రింగ్ ఉన్న కేస్ ("wke" -> 3)
    assert length_of_longest_substring("pwwkew") == 3, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఖాళీ స్ట్రింగ్ కేస్
    assert length_of_longest_substring("") == 0, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: స్పేస్‌తో కూడిన కేస్
    assert length_of_longest_substring(" ") == 1, "Test case 5 failed"

    # టెస్ట్ కేస్ 6: రెండు వేర్వేరు అక్షరాలు
    assert length_of_longest_substring("au") == 2, "Test case 6 failed"

    print("All Longest Substring Without Repeating Characters assertions passed successfully with O(N) complexity!")