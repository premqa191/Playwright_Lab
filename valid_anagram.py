def is_anagram(s: str, t: str) -> bool:
    """
    Time Complexity: O(N) - స్ట్రింగ్ పొడవు ఆధారంగా లీనియర్ సమయంలో పూర్తవుతుంది.
    Space Complexity: O(1) - ఇంగ్లీష్ ఆల్ఫాబెట్స్ (గరిష్టంగా 26 అక్షరాలు) మాత్రమే ఉంటాయి కాబట్టి స్థిరమైన మెమరీ.
    """
    # బౌండరీ కేస్: పొడవులు భిన్నంగా ఉంటే వెంటనే నిష్క్రమిస్తుంది
    if len(s) != len(t):
        return False

    char_counts = {}

    # స్ట్రింగ్ 's' లోని అక్షరాల ఫ్రీక్వెన్సీని లెక్కించడం
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1

    # స్ట్రింగ్ 't' ద్వారా ఫ్రీక్వెన్సీని ధృవీకరించడం
    for char in t:
        if char not in char_counts or char_counts[char] == 0:
            return False
        char_counts[char] -= 1

    return True

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: వాలిడ్ అనగ్రామ్
    assert is_anagram("anagram", "nagaram") is True, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: ఇన్వాలిడ్ అనగ్రామ్
    assert is_anagram("rat", "car") is False, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: వేర్వేరు పొడవులు ఉన్న కేస్
    assert is_anagram("a", "ab") is False, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: పునరావృత అక్షరాలు తప్పుగా ఉన్న కేస్
    assert is_anagram("aa", "a") is False, "Test case 4 failed"

    print("All Valid Anagram assertions passed successfully with O(N) time complexity!")