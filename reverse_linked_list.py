class ListNode:
    """సింగిల్లీ లింక్డ్ లిస్ట్ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, next_node: "ListNode" = None):
        self.val = val
        self.next = next_node

def reverse_list(head: ListNode) -> ListNode:
    """
    Time Complexity: O(N) - లింక్డ్ లిస్ట్‌లోని ప్రతి నోడ్‌ను ఒకేసారి సందర్శిస్తుంది.
    Space Complexity: O(1) - కేవలం మూడు పాయింటర్లతో ఇన్-ప్లేస్ రివర్సల్ చేస్తుంది.
    """
    prev = None
    curr = head

    while curr:
        next_temp = curr.next  # తదుపరి నోడ్ రిఫరెన్స్ భద్రపరచడం
        curr.next = prev       # పాయింటర్‌ను వెనుకకు తిప్పడం
        prev = curr            # prev ను ముందుకు జరపడం
        curr = next_temp       # curr ను ముందుకు జరపడం

    return prev

# టెస్టింగ్ కోసం సహాయక ఫంక్షన్లు
def list_to_linked_list(elements: list[int]) -> ListNode:
    dummy = ListNode(0)
    current = dummy
    for val in elements:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_list_to_list(head: ListNode) -> list[int]:
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక లిస్ట్ [1, 2, 3, 4, 5] -> [5, 4, 3, 2, 1]
    head1 = list_to_linked_list([1, 2, 3, 4, 5])
    reversed_head1 = reverse_list(head1)
    assert linked_list_to_list(reversed_head1) == [5, 4, 3, 2, 1], "Test 1 Failed"

    # టెస్ట్ కేస్ 2: రెండు నోడ్స్ మాత్రమే ఉన్నప్పుడు [1, 2] -> [2, 1]
    head2 = list_to_linked_list([1, 2])
    reversed_head2 = reverse_list(head2)
    assert linked_list_to_list(reversed_head2) == [2, 1], "Test 2 Failed"

    # టెస్ట్ కేస్ 3: ఒకే నోడ్ ఉన్నప్పుడు [10] -> [10]
    head3 = list_to_linked_list([10])
    reversed_head3 = reverse_list(head3)
    assert linked_list_to_list(reversed_head3) == [10], "Test 3 Failed"

    # టెస్ట్ కేస్ 4: ఖాళీ లిస్ట్ (None)
    head4 = list_to_linked_list([])
    reversed_head4 = reverse_list(head4)
    assert linked_list_to_list(reversed_head4) == [], "Test 4 Failed"

    print("All Reverse Linked List assertions passed successfully with O(N) time and O(1) space complexity!")