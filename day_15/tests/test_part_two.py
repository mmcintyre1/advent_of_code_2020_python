import pytest

from day_15.part_one import speak_n_say


def test_speak_n_say_one():
    nums = [1, 3, 2]
    assert speak_n_say(nums, 30000000) == 2578


def test_speak_n_say_two():
    nums = [2, 1, 3]
    assert speak_n_say(nums, 30000000) == 3544142


def test_speak_n_say_three():
    nums = [1, 2, 3]
    assert speak_n_say(nums, 30000000) == 261214


def test_speak_n_say_four():
    nums = [2, 3, 1]
    assert speak_n_say(nums, 30000000) == 6895259


def test_speak_n_say_five():
    nums = [3, 2, 1]
    assert speak_n_say(nums, 30000000) == 18


def test_speak_n_say_six():
    nums = [3, 1, 2]
    assert speak_n_say(nums, 30000000) == 362


if __name__ == '__main__':
    pytest.main()