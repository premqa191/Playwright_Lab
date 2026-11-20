def climb_stairs(n: int) -> int:
    """
    Time Complexity: O(N) - 1 నుండి n వరకు ఒకే ఒక లూప్ నడుస్తుంది.
    Space Complexity: O(1) - పూర్తి అరే నిల్వ చేయకుండా కేవలం రెండు వేరియబుల్స్ మాత్రమే వాడతాం.
    """
    if n <= 2:
        return n

    # బేస్ కేసెస్: n=1 కి 1 మార్గం, n=2 కి 2 మార్గాలు
    prev2 = 1  # ways(i - 2)
    prev1 = 2  # ways(i - 1)

    for _ in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current

    return prev1

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: n = 1
    assert climb_stairs(1) == 1, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: n = 2
    assert climb_stairs(2) == 2, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: n = 3
    assert climb_stairs(3) == 3, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: n = 4
    assert climb_stairs(4) == 5, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: n = 5
    assert climb_stairs(5) == 8, "Test case 5 failed"

    # టెస్ట్ కేస్ 6: n = 10
    assert climb_stairs(10) == 89, "Test case 6 failed"

    print("All Climbing Stairs assertions passed successfully with O(N) Time and O(1) Space DP!")