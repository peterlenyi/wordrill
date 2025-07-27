# Wordrill © 2025 by Peter Lényi is licensed under GNU GPL v3
# License: https://www.gnu.org/licenses/gpl-3.0.html

from wordrill.word import test_target_word

EASY_MODE = "EASY"
HARD_MODE = "HARD"

TRANSLATION_DICTIONARY = {
        "dog": ["Hund"],
        "dogs": ["Hünde"],
    }


def test_test_target_word_returns_failure_for_wrong_word_in_hard_mode():
    assert not test_target_word("dog", "", TRANSLATION_DICTIONARY, HARD_MODE)


def test_test_target_word_returns_success_for_right_case_in_hard_mode():
    assert test_target_word("dog", "Hund", TRANSLATION_DICTIONARY, HARD_MODE)


def test_test_target_word_returns_failure_for_wrong_case_in_hard_mode():
    assert not test_target_word("dog", "hund", TRANSLATION_DICTIONARY, HARD_MODE)


def test_test_target_word_returns_success_for_right_accent_in_hard_mode():
    assert test_target_word("dogs", "Hünde", TRANSLATION_DICTIONARY, HARD_MODE)


def test_test_target_word_returns_failure_for_wrong_accent_in_hard_mode():
    assert not test_target_word("dogs", "Hunde", TRANSLATION_DICTIONARY, HARD_MODE)


def test_test_target_word_returns_failure_for_wrong_word_in_easy_mode():
    assert not test_target_word("dog", "", TRANSLATION_DICTIONARY, EASY_MODE)


def test_test_target_word_returns_success_for_right_case_in_easy_mode():
    assert test_target_word("dog", "Hund", TRANSLATION_DICTIONARY, EASY_MODE)


def test_test_target_word_returns_success_for_wrong_case_in_easy_mode():
    assert test_target_word("dog", "hund", TRANSLATION_DICTIONARY, EASY_MODE)


def test_test_target_word_returns_success_for_right_accent_in_easy_mode():
    assert test_target_word("dogs", "Hünde", TRANSLATION_DICTIONARY, EASY_MODE)


def test_test_target_word_returns_success_for_wrong_accent_in_easy_mode():
    assert test_target_word("dogs", "Hunde", TRANSLATION_DICTIONARY, EASY_MODE)
