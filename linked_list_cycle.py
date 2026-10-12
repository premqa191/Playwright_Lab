class ListNode:
    """సింగిల్లీ లింక్డ్ లిస్ట్ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, next_node: "ListNode" = None):
        self.val = val
        self.next = next_node

def has_cycle(head: ListNode) -> bool:
    """
    Time Complexity: O(N) - లూప్ ఉన్నా లేకపోయినా పాయింటర్లు O(N) దశల్లోనే ఫలితాన్ని తేలుస్తాయి.
    Space Complexity: O(1) - అదనపు డేటా స్ట్రక్చర్స్ లేకుండా స్థిరమైన మెమరీతో నడుస్తుంది.
    """
    if not head or not head.next:
        return False

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next          # 1 అడుగు
        fast = fast.next.next     # 2 అడుగులు

        # రెండు పాయింటర్లు ఒకే నోడ్ వద్ద కలిస్తే సైకిల్ ఉన్నట్లు లెక్క
        if slow == fast:
            return True

    return False

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: సైకిల్ ఉన్న లింక్డ్ లిస్ట్ [3 -> 2 -> 0 -> -4 -> (తిరిగి 2)]
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # లూప్ ఏర్పరచడం

    assert has_cycle(node1) is True, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: సైకిల్ లేని సరళమైన లిస్ట్ [1 -> 2 -> None]
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    assert has_cycle(n1) is False, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: కేవలం ఒకే నోడ్ ఉండి సైకిల్ లేనప్పుడు [1 -> None]
    single_node = ListNode(1)
    assert has_cycle(single_node) is False, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఒకే నోడ్ తనకే తిరిగి పాయింట్ చేసుకుంటున్నప్పుడు [1 -> 1]
    self_loop = ListNode(1)
    self_loop.next = self_loop
    assert has_cycle(self_loop) is True, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: ఖాళీ లిస్ట్ (None)
    assert has_cycle(None) is False, "Test case 5 failed"

    print("All Linked List Cycle assertions passed successfully with Floyd's O(1) space algorithm!")