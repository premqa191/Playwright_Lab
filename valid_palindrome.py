def is_palindrome(s: str) -> bool:
    """
    Time Complexity: O(N) - స్ట్రింగ్‌ను ఎడమ, కుడి నుండి ఒకేసారి స్కాన్ చేస్తుంది.
    Space Complexity: O(1) - అదనపు స్ట్రింగ్ మెమరీ లేకుండా పాయింటర్లతోనే పనిచేస్తుంది.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # ఎడమవైపు నాన్-ఆల్ఫాన్యూమరిక్ క్యారెక్టర్లను దాటవేయడం
        while left < right and not s[left].isalnum():
            left += 1

        # కుడివైపు నాన్-ఆల్ఫాన్యూమరిక్ క్యారెక్టర్లను దాటవేయడం
        while left < right and not s[right].isalnum():
            right -= 1

        # అక్షరాలను లోయర్‌కేస్‌లోకి మార్చి సరిపోల్చడం
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: సంక్లిష్టమైన విరామ చిహ్నాలు, స్పేస్‌లు ఉన్న కేస్
    assert is_palindrome("A man, a plan, a canal: Panama") is True, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: పాలిండ్రోమ్ కాని కేస్
    assert is_palindrome("race a car") is False, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: కేవలం స్పేస్ మాత్రమే ఉన్న ఖాళీ కేస్
    assert is_palindrome(" ") is True, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: నంబర్లు కలిపి ఉన్న కేస్
    assert is_palindrome("0P") is False, "Test case 4 failed"

    print("All Valid Palindrome assertions passed successfully with O(1) space complexity!")