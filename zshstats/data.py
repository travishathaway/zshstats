import os
from pathlib import Path


def read_zsh_history_lines() -> list:
    zsh_history_file = os.path.join(Path().home(), '.zsh_history')
    encoding = 'latin'

    with open(zsh_history_file, encoding=encoding) as fp:
        return fp.readlines()
