# Wordrill © 2025 by Peter Lényi is licensed under GNU GPL v3
# License: https://www.gnu.org/licenses/gpl-3.0.html

from load import parse_information_dictionary, parse_translation_dictionary


def test_parse_information_dictionary():
    sample = "\n"
    sample += "[animals]\n"
    sample += "cat = pl. cats\n"
    sample += "dog = pl. dogs\n"
    sample += "fish = pl. fish\n"
    sample += "mouse = pl. mice\n"

    wanted = {
        'cat': 'pl. cats',
        'dog': 'pl. dogs',
        'fish': 'pl. fish',
        'mouse': 'pl. mice'
    }

    actual = parse_information_dictionary(sample)

    assert actual == wanted


def test_parse_translation_dictionary():
    sample = "\n"
    sample += "[animals]\n"
    sample += "cat = Katze, Kater\n"
    sample += "dog = Hund, Hündin\n"
    sample += "fish = Fisch\n"
    sample += "mouse = Maus\n"

    wanted = {
        'cat': ['Katze', 'Kater'],
        'dog': ['Hund', 'Hündin'],
        'fish': ['Fisch'],
        'mouse': ['Maus']
    }

    actual = parse_translation_dictionary(sample)

    assert actual == wanted
