# Wordrill © 2025 by Peter Lényi is licensed under GNU GPL v3
# License: https://www.gnu.org/licenses/gpl-3.0.html

from random import choice
from unidecode import unidecode


def pick_source_word(translation_dictionary) -> str:
    return choice(list(translation_dictionary.keys()))


def test_target_word(source_word, target_word, translation_dictionary, test_mode) -> bool:
    target_words = translation_dictionary.get(source_word)

    if test_mode == "EASY":
        target_word = unidecode(target_word).lower()
        target_words = [unidecode(target_word).lower() for target_word in target_words]

    return target_word in target_words
