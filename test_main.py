from main import get_weather


def test_get_weather():
    assert get_weather(20) == 'cold'
    assert get_weather(21) == 'hot'
