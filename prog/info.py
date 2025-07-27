# Wordrill © 2025 by Peter Lényi is licensed under GNU GPL v3
# License: https://www.gnu.org/licenses/gpl-3.0.html


def get_copy_text() -> str:
    copy_text = "\n"
    copy_text += "Wordrill 1.0.4 © 2025 by Peter Lényi \n"
    copy_text += "\n"
    copy_text += "This program is free software: you can redistribute it and/or modify \n"
    copy_text += "it under the terms of the GNU General Public License as published by \n"
    copy_text += "the Free Software Foundation, either version 3 of the license, or \n"
    copy_text += "(at your option) any later version. \n"
    copy_text += "\n"
    copy_text += "This program is distributed in the hope that it will be useful, \n"
    copy_text += "but WITHOUT ANY WARRANTY; without even the implied warranty of \n"
    copy_text += "MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the \n"
    copy_text += "GNU General Public License for more details."
    copy_text += "\n"
    copy_text += "You should have received a copy of the GNU General Public License \n"
    copy_text += "along with this program. If not, see <https://www.gnu.org/licenses/>. \n"
    return copy_text


def get_help_text() -> str:
    help_text = "\n"
    help_text += "    /exit - exit the application \n"
    help_text += "    /help - show this help text \n"
    help_text += "    /test - translate words (from locale to locale) \n"
    help_text += "    /hard - check exact translations (in test loop) \n"
    help_text += "    /easy - ignore accents and case (in test loop) \n"
    return help_text
