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
    last_key = None

    for line in text.splitlines():

        if line.strip() == "":
            last_key = None
            continue

        if line.strip().startswith(("#", ";", "[")):
            last_key = None
            continue

        if '=' in line:
            key, value = line.split('=', 1)
            dictionary[key.strip()] = value.strip()
            last_key = key.strip()
            continue

        if last_key:
            dictionary[last_key] += f"\n{line.strip()}"

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
    last_key = None

    for line in text.splitlines():

        if line.isspace():
            last_key = None
            continue

        if line.strip().startswith(("#", ";", "[")):
            last_key = None
            continue

        if '=' in line:
            key, values = line.split('=', 1)
            values_list = [value.strip() for value in values.split(',')]
            dictionary[key.strip()] = values_list
            last_key = key.strip()
            continue

        dictionary[last_key].extend([value.strip() for value in line.split(',')])

    return dictionary
