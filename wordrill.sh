#!/usr/bin/env bash

# Wordrill © 2025 by Peter Lényi is licensed under GNU GPL v3
# License: https://www.gnu.org/licenses/gpl-3.0.html

set -e
DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
exec env -C "$DIR" python3 -m prog.main "$@"
