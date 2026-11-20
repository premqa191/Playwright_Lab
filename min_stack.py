class MinStack:
    """
    Time Complexity: All operations (push, pop, top, get_min) run in O(1) constant time.
    Space Complexity: O(N) - కనిష్ట విలువలను ట్రాక్ చేయడానికి అదనపు స్టాక్‌ను నిర్వహిస్తుంది.
    """
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # min_stack ఖాళీగా ఉన్నా లేదా కొత్త విలువ ప్రస్తుత మినిమమ్ కంటే చిన్నదైనా/సమానమైనా యాడ్ చేయడం
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return
        val = self.stack.pop()
        # పాప్ చేసిన ఎలిమెంట్ ప్రస్తుత మినిమమ్ అయితే సహాయక స్టాక్ నుండి కూడా తొలగించడం
        if val == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        raise IndexError("Stack is empty")

    def get_min(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        raise IndexError("Stack is empty")

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక స్క్రీనింగ్ ఫ్లో
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    assert min_stack.get_min() == -3, "Test 1 Failed: Expected -3"

    min_stack.pop()
    assert min_stack.top() == 0, "Test 1 Failed: Expected Top 0"
    assert min_stack.get_min() == -2, "Test 1 Failed: Expected -2 after pop"

    # టెస్ట్ కేస్ 2: ఒకే విలువలు మళ్లీ మళ్లీ వచ్చినప్పుడు
    duplicate_stack = MinStack()
    duplicate_stack.push(5)
    duplicate_stack.push(5)
    duplicate_stack.push(3)
    duplicate_stack.push(3)
    assert duplicate_stack.get_min() == 3, "Test 2 Failed"
    duplicate_stack.pop()
    assert duplicate_stack.get_min() == 3, "Test 2 Failed: Second 3 should still keep min as 3"
    duplicate_stack.pop()
    assert duplicate_stack.get_min() == 5, "Test 2 Failed: Min should revert to 5"

    # టెస్ట్ కేస్ 3: ఒకే ఎలిమెంట్ ఉన్నప్పుడు
    single_stack = MinStack()
    single_stack.push(42)
    assert single_stack.get_min() == 42
    assert single_stack.top() == 42

    print("All Min Stack assertions passed successfully with strict O(1) time complexity!")