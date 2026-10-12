def is_valid(s: str) -> bool:
    """
    Time Complexity: O(N) - స్ట్రింగ్‌ను ఒకే ఒకసారి స్కాన్ చేస్తుంది.
    Space Complexity: O(N) - బ్రాకెట్లను భద్రపరచడానికి స్టాక్ వాడుతుంది.
    """
    # బ్రాకెట్ మ్యాపింగ్ (Closing -> Opening)
    bracket_map = {")": "(", "}": "{", "]": "["}
    stack = []

    for char in s:
        if char in bracket_map:
            # క్లోజింగ్ బ్రాకెట్ వచ్చినప్పుడు స్టాక్ పైభాగాన్ని పరిశీలించడం
            top_element = stack.pop() if stack else '#'
            if top_element != bracket_map[char]:
                return False
        else:
            # ఓపెనింగ్ బ్రాకెట్‌ను స్టాక్‌లో భద్రపరచడం
            stack.append(char)

    # స్టాక్ ఖాళీగా ఉంటేనే బ్రాకెట్లు అన్నీ సరైన క్రమంలో పూర్తయినట్లు
    return len(stack) == 0

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక జంటలు
    assert is_valid("()") is True, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: బహుళ రకాల బ్రాకెట్లు వరుసగా
    assert is_valid("()[]{}") is True, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: సరిపోలని బ్రాకెట్లు
    assert is_valid("(]") is False, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: నెస్టెడ్ సరైన క్రమం
    assert is_valid("{[]}") is True, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: తప్పుడు నెస్టెడ్ ఆర్డర్
    assert is_valid("([)]") is False, "Test case 5 failed"

    # టెస్ట్ కేస్ 6: కేవలం ఓపెన్ బ్రాకెట్ మాత్రమే ఉన్నప్పుడు
    assert is_valid("[") is False, "Test case 6 failed"

    # టెస్ట్ కేస్ 7: కేవలం క్లోజింగ్ బ్రాకెట్ మాత్రమే ఉన్నప్పుడు
    assert is_valid("]") is False, "Test case 7 failed"

    print("All Valid Parentheses assertions passed successfully with O(N) time and space complexity!")