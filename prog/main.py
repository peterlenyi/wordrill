# Wordrill © 2025 by Peter Lényi is licensed under GNU GPL v3
# License: https://www.gnu.org/licenses/gpl-3.0.html

from info import get_copy_text, get_help_text
from load import load_information_dictionary, load_translation_dictionary
from word import test_target_word, pick_source_word


def info_loop():
    while True:
        inst = input("Enter instruction:\n").strip()
        if inst.startswith("/exit"):
            return
        if inst.startswith("/test"):
            try:
                _, source_locale, target_locale = inst.split(" ")
                test_loop(source_locale, target_locale)
                continue
            except ValueError:
                print("Source and/or target locale isn't specified.\n")
                continue
            except FileNotFoundError:
                print("Source and/or target dictionary isn't installed.\n")

        print(get_help_text())


def test_loop(source_locale, target_locale):
    test_mode = "HARD"

    translation_dictionary = load_translation_dictionary(source_locale, target_locale)
    information_dictionary = load_information_dictionary(target_locale)

    while True:
        source_word = pick_source_word(translation_dictionary)
        target_word = input(f"Enter translation for [ {source_word} ]:\n")

        if target_word.startswith("/easy"):
            test_mode = "EASY"
            continue

        if target_word.startswith("/hard"):
            test_mode = "HARD"
            continue

        if test_target_word(source_word, target_word, translation_dictionary, test_mode):
            print(f"Right!\n{information_dictionary[target_word]}\n")
            continue
        else:
            print(f"Wrong!\n{translation_dictionary[source_word]}\n")
            continue


if __name__ == '__main__':
    print(get_copy_text())
    info_loop()
