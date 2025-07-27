# Wordrill © 2025 by Peter Lényi is licensed under GNU GPL v3
# License: https://www.gnu.org/licenses/gpl-3.0.html

import os

from platformdirs import user_config_dir


def load_information_dictionary(locale) -> dict:
    file_name = f"wordrill-{locale}.ini"
    file_dir = user_config_dir("wordrill", False, ensure_exists=True)
    file_path = os.path.join(file_dir, file_name)
    print(file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    return parse_information_dictionary(text)


def parse_information_dictionary(text) -> dict:
    dictionary = {}

    for line in text.splitlines():
        if line.startswith("#") or line.startswith(";"):
            continue
        if '=' in line:
            key, value = line.split('=', 1)
            dictionary[key.strip()] = value.strip()

    return dictionary


def load_translation_dictionary(source, target) -> dict:
    file_name = f"wordrill-{source}-x-{target}.ini"
    file_dir = user_config_dir("wordrill", False, ensure_exists=True)
    file_path = os.path.join(file_dir, file_name)
    print(file_path)

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    return parse_translation_dictionary(text)


def parse_translation_dictionary(text) -> dict:
    dictionary = {}

    for line in text.splitlines():
        if line.startswith("#") or line.startswith(";"):
            continue
        if '=' in line:
            key, values = line.split('=', 1)
            values_list = [value.strip() for value in values.split(',')]
            dictionary[key.strip()] = values_list

    return dictionary
