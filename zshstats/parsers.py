from datetime import datetime
from typing import Iterable, Iterator, Union

from zshstats.types import ZshHstRow


def parse_rows(iterable: Iterable) -> Iterator:
    """
    We used this function to parse each row. We're interested in the command and
    the time stamp.
    """
    return (
        parse_single_row(row) for row in iterable
    )


def parse_single_row(row: str) -> ZshHstRow:
    return ZshHstRow(
        datetime=parse_date_field(row),
        cmd=parse_cmd(row),
        args=parse_args(row),
        sudo_cmd=parse_sudo_cmd(row)
    )


def parse_date_field(row: str) -> Union[datetime, None]:
    try:
        return datetime.fromtimestamp(int(row[1:12]))
    except IndexError:
        return


def parse_cmd(row: str) -> Union[str, None]:
    try:
        return row[15:].split()[0]
    except IndexError:
        return


def parse_sudo_cmd(row: str) -> Union[str, None]:
    try:
        return row.split('sudo')[1].split()[0].strip()
    except IndexError:
        return


def parse_args(row: str) -> Union[tuple[str], None]:
    try:
        return tuple(row[15:].split()[1:])
    except IndexError:
        return
