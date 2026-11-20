# test_first.py

def test_basic_addition():
    """ఒక సాధారణ కూడిక సరిగ్గా ఉందో లేదో తనిఖీ చేస్తుంది"""
    assert 2 + 3 == 5

def test_string_uppercase():
    """స్ట్రింగ్ మెథడ్స్ పనిచేస్తున్నాయో లేదో తనిఖీ చేస్తుంది"""
    name = "pytest"
    assert name.upper() == "PYTEST"

def test_list_membership():
    """జాబితాలో ఎలిమెంట్ ఉందో లేదో చూస్తుంది"""
    tools = ["selenium", "playwright", "pytest"]
    assert "pytest" in tools