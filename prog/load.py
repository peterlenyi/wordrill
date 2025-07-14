# Wordrill © 2025 by Peter Lényi is licensed under GNU GPL v3
# License: https://www.gnu.org/licenses/gpl-3.0.html

import os


def load_information_dictionary(locale) -> dict:
    file_name = f"Wordrill-{locale}.ini"
    file_path = os.path.join("..", "dict", file_name)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    return parse_information_dictionary(text)


def parse_information_dictionary(text) -> dict:
    dictionary = {}
    
    for line in text.splitlines():
        if '=' in line:
            key, value = line.split('=', 1)
            dictionary[key.strip()] = value.strip()
    
    return dictionary


def load_translation_dictionary(source, target) -> dict:
    file_name = f"Wordrill-{source}-x-{target}.ini"
    file_path = os.path.join("..", "dict", file_name)

    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()

    return parse_information_dictionary(text)


def parse_translation_dictionary(text) -> dict:
    dictionary = {}
    
    for line in text.splitlines():
        if '=' in line:
            key, values = line.split('=', 1)
            values_list = [value.strip() for value in values.split(',')]
            dictionary[key.strip()] = values_list
    
    return dictionary
