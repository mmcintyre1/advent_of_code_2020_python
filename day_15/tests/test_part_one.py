import pytest

from day_15.part_one import speak_n_say


def test_speak_n_say_one():
    nums = [1, 3, 2]
    assert speak_n_say(nums, 2020) == 1


def test_speak_n_say_two():
    nums = [2, 1, 3]
    assert speak_n_say(nums, 2020) == 10


def test_speak_n_say_three():
    nums = [1, 2, 3]
    assert speak_n_say(nums, 2020) == 27


def test_speak_n_say_four():
    nums = [2, 3, 1]
    assert speak_n_say(nums, 2020) == 78


def test_speak_n_say_five():
    nums = [3, 2, 1]
    assert speak_n_say(nums, 2020) == 438


def test_speak_n_say_six():
    nums = [3, 1, 2]
    assert speak_n_say(nums, 2020) == 1836


if __name__ == '__main__':
    pytest.main()