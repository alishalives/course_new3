from json import JSONDecodeError
import utils
import pytest


def test_load_json():
    with pytest.raises(FileNotFoundError):
        utils.load_json("")
    with pytest.raises(JSONDecodeError):
        utils.load_json("main.py")


def test_state_sorted_data():
    assert utils.state_sorted_data(utils.load_json("operations.json"), 3) == []


def test_time_sorted_data():
    assert utils.time_sorted_data(utils.load_json("json_for_test.json")) == [{"date": "19.10.2020"}, {"date": "10.10.2019"}]


def test_card_with_code():
    assert utils.card_with_code("1234567890") == "1234 56** **** **** 7890"
    assert utils.card_with_code("Master Card 1234567890") == "Master Card 1234 56** **** **** 7890"
    assert utils.card_with_code("Master 1234567890") == "Master 1234 56** **** **** 7890"


def test_account_with_code():
    assert utils.account_with_code("1234567890") == "**** **** **** **** 7890"
    assert utils.account_with_code("Master Card 1234567890") == "Master Card **** **** **** **** 7890"
    assert utils.account_with_code("Master 1234567890") == "Master **** **** **** **** 7890"

