# Lab#2 - Test design - designing practical test scenarios and test cases
# Student name: Mr.Panyawut Saengdaeng
# Student ID: 653380138-3

import pytest

MINIMUM = 500
MIDRANGE = 700
MAXIMUM = 3500
FREE_ICECREAM = "Free ice cream cone = "
FREE_CAKE = "Free chocolate cake = "
NO_GIFT = "Thank you and see you next time"
ERROR = "Error: Invalid input"

def get_promotion(total_cost):
    if not isinstance(total_cost, int) or total_cost < 0:
        return ERROR

    num_icecream = 0
    num_cake = 0

    if total_cost >= MINIMUM:
        while total_cost > 0:
            if total_cost >= MAXIMUM:
                num_icecream += total_cost // MAXIMUM
                num_cake += total_cost // MAXIMUM
                total_cost %= MAXIMUM
            elif total_cost >= MIDRANGE:
                num_cake += total_cost // MIDRANGE
                total_cost %= MIDRANGE
            elif total_cost >= MINIMUM:
                num_icecream += total_cost // MINIMUM
                total_cost %= MINIMUM
            else:
                break

        if num_icecream > 0 and num_cake > 0:
            return f"{FREE_ICECREAM}{num_icecream} and {FREE_CAKE}{num_cake}"
        elif num_cake > 0:
            return f"{FREE_CAKE}{num_cake}"
        else:
            return f"{FREE_ICECREAM}{num_icecream}"
    else:
        return NO_GIFT

# TS001 Test Cases
@pytest.mark.parametrize("total_cost, expected", [
    (150, NO_GIFT),
    (500, f"{FREE_ICECREAM}1"),
    (700, f"{FREE_CAKE}1"),
    (1200, f"{FREE_ICECREAM}1 and {FREE_CAKE}1"),
    (1400, f"{FREE_ICECREAM}1 and {FREE_CAKE}1"),
    (2400, f"{FREE_ICECREAM}2 and {FREE_CAKE}2"),
    (3500, f"{FREE_ICECREAM}1 and {FREE_CAKE}1")
])
def test_ts001(total_cost, expected):
    assert get_promotion(total_cost) == expected

# TS002 Test Cases
@pytest.mark.parametrize("total_cost, expected", [
    (499, NO_GIFT),
    (699, f"{FREE_ICECREAM}1"),
    (1199, f"{FREE_CAKE}1")
])
def test_ts002(total_cost, expected):
    assert get_promotion(total_cost) == expected

# TS003 Test Cases
@pytest.mark.parametrize("total_cost, expected", [
    ("abc", ERROR),
    (-100, ERROR)
])
def test_ts003(total_cost, expected):
    assert get_promotion(total_cost) == expected

if __name__ == "__main__":
    pytest.main()
