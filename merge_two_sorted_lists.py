class ListNode:
    """సింగిల్లీ లింక్డ్ లిస్ట్ నోడ్ నిర్మాణం"""
    def __init__(self, val: int = 0, next_node: "ListNode" = None):
        self.val = val
        self.next = next_node

def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
    """
    Time Complexity: O(N + M) - రెండు లిస్ట్‌లలోని అన్ని నోడ్స్‌ను ఒక్కోసారి ప్రాసెస్ చేస్తుంది.
    Space Complexity: O(1) - కొత్త నోడ్స్ నిర్మించకుండా ఉన్న పాయింటర్లను మాత్రమే మారుస్తుంది.
    """
    dummy = ListNode(0)
    current = dummy

    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    # మిగిలిపోయిన లిస్ట్‌ను డైరెక్ట్‌గా జోడించడం
    current.next = list1 if list1 else list2

    return dummy.next

# టెస్టింగ్ కోసం సహాయక ఫంక్షన్లు
def list_to_linked_list(elements: list[int]) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    for val in elements:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head: ListNode) -> list[int]:
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక సార్టెడ్ లిస్ట్‌లు
    l1 = list_to_linked_list([1, 2, 4])
    l2 = list_to_linked_list([1, 3, 4])
    merged1 = merge_two_lists(l1, l2)
    assert linked_list_to_list(merged1) == [1, 1, 2, 3, 4, 4], "Test 1 Failed"

    # టెస్ట్ కేస్ 2: రెండు లిస్ట్‌లూ ఖాళీగా ఉన్నప్పుడు
    l3 = list_to_linked_list([])
    l4 = list_to_linked_list([])
    merged2 = merge_two_lists(l3, l4)
    assert linked_list_to_list(merged2) == [], "Test 2 Failed"

    # టెస్ట్ కేస్ 3: ఒక లిస్ట్ ఖాళీగా, మరొకటి విలువలతో ఉన్నప్పుడు
    l5 = list_to_linked_list([])
    l6 = list_to_linked_list([0])
    merged3 = merge_two_lists(l5, l6)
    assert linked_list_to_list(merged3) == [0], "Test 3 Failed"

    # టెస్ట్ కేస్ 4: వేర్వేరు పరిమాణాలు మరియు విలువలు ఉన్న లిస్ట్‌లు
    l7 = list_to_linked_list([5, 10, 15, 20])
    l8 = list_to_linked_list([2, 3, 25])
    merged4 = merge_two_lists(l7, l8)
    assert linked_list_to_list(merged4) == [2, 3, 5, 10, 15, 20, 25], "Test 4 Failed"

    print("All Merge Two Sorted Lists assertions passed successfully with O(N + M) time and O(1) space complexity!")