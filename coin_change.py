def coin_change(coins: list[int], amount: int) -> int:
    """
    Time Complexity: O(amount * len(coins)) - ప్రతి మొత్తానికి అన్ని నాణేలను పరీక్షిస్తాం.
    Space Complexity: O(amount) - DP టేబుల్ కోసం amount + 1 స్థలాన్ని కేటాయిస్తాం.
    """
    # గరిష్టంగా అవసరమయ్యే నాణేల కంటే పెద్ద విలువతో (amount + 1) ప్రారంభించడం
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # బేస్ కేస్: 0 మొత్తానికి 0 నాణేలు

    for a in range(1, amount + 1):
        for c in coins:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])

    # dp[amount] మారకుండా అలాగే ఉంటే ఆ మొత్తాన్ని తయారు చేయడం అసాధ్యం
    return dp[amount] if dp[amount] != amount + 1 else -1

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక కేస్ (5 + 5 + 1 = 11 -> 3 నాణేలు)
    assert coin_change([1, 2, 5], 11) == 3, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: సాధ్యం కాని మొత్తం
    assert coin_change([2], 3) == -1, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: మొత్తం సున్నా అయినప్పుడు
    assert coin_change([1], 0) == 0, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: గ్రీడీ పద్ధతి విఫలమయ్యే కేస్ (సరియైన సమాధానం 3+3=6 -> 2 నాణేలు)
    assert coin_change([1, 3, 4], 6) == 2, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: పెద్ద నాణేలు ఉన్నప్పుడు
    assert coin_change([186, 419, 83, 408], 6249) == 20, "Test case 5 failed"

    print("All Coin Change assertions passed successfully with O(amount * N) DP!")