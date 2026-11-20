def max_profit(prices: list[int]) -> int:
    """
    Time Complexity: O(N) - ధరల జాబితాను ఒకే ఒక పాస్‌లో స్కాన్ చేస్తుంది.
    Space Complexity: O(1) - స్థిరమైన మెమరీతో నడుస్తుంది.
    """
    min_price = float('inf')
    max_profit_earned = 0

    for price in prices:
        if price < min_price:
            # అతి తక్కువ కొనుగోలు ధరను అప్‌డేట్ చేయడం
            min_price = price
        else:
            # ప్రస్తుత రోజు అమ్మితే వచ్చే లాభాన్ని అంచనా వేయడం
            current_profit = price - min_price
            if current_profit > max_profit_earned:
                max_profit_earned = current_profit

    return max_profit_earned

if __name__ == "__main__":
    # టెస్ట్ కేస్ 1: ప్రామాణిక కేస్ (లాభం: 6 - 1 = 5)
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5, "Test case 1 failed"

    # టెస్ట్ కేస్ 2: ధరలు తగ్గుతూనే ఉన్న కేస్ (లాభం పొందే అవకాశం లేదు)
    assert max_profit([7, 6, 4, 3, 1]) == 0, "Test case 2 failed"

    # టెస్ట్ కేస్ 3: రెండు రోజులు మాత్రమే ఉన్న కేస్ (లాభం: 4 - 2 = 2)
    assert max_profit([2, 4, 1]) == 2, "Test case 3 failed"

    # టెస్ట్ కేస్ 4: ఒకే ఒక రోజు ధర ఉన్న కేస్
    assert max_profit([5]) == 0, "Test case 4 failed"

    # టెస్ట్ కేస్ 5: చివరి రోజున భారీ పెరుగుదల ఉన్న కేస్
    assert max_profit([3, 2, 6, 5, 0, 3]) == 4, "Test case 5 failed"

    print("All Best Time to Buy and Sell Stock assertions passed successfully with O(N) time and O(1) space complexity!")