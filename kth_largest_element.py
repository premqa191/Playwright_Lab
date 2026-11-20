import heapq
from collections import Counter

def top_k_frequent(nums: list[int], k: int) -> list[int]:
    """
    Time Complexity: O(N log K) - ఫ్రీక్వెన్సీ లెక్కించడానికి O(N), k సైజు గల హీప్‌ను నిర్వహించడానికి O(N log K).
    Space Complexity: O(N + K) - డిక్షనరీలో O(N) మూలకాలు, హీప్‌లో O(K) మూలకాలు ఉంటాయి.
    """
    count_map = Counter(nums)
    min_heap = []

    for num, freq in count_map.items():
        heapq.heappush(min_heap, (freq, num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for freq, num in min_heap]

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక కేస్
    res1 = top_k_frequent([1, 1, 1, 2, 2, 3], 2)
    assert sorted(res1) == [1, 2], f"Test case 1 failed: got {res1}"

    # టెస్ట్ కేస్ 2: ఒకే ఒక మూలకం ఉన్నప్పుడు
    res2 = top_k_frequent([1], 1)
    assert res2 == [1], f"Test case 2 failed: got {res2}"

    # టెస్ట్ కేస్ 3: రుణ సంఖ్యలు మరియు సమాన పునరావృతాలు
    res3 = top_k_frequent([-1, -1, 2, 2, 3], 2)
    assert sorted(res3) == [-1, 2], f"Test case 3 failed: got {res3}"

    # టెస్ట్ కేస్ 4: అన్ని సంఖ్యలూ వేర్వేరుగా ఉన్నప్పుడు
    res4 = top_k_frequent([4, 5, 6, 7], 1)
    assert len(res4) == 1 and res4[0] in [4, 5, 6, 7], "Test case 4 failed"

    print("All Top K Frequent Elements assertions passed successfully with O(N log K) Heap!")