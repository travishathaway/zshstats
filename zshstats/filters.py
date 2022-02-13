from datetime import datetime
from typing import Iterator, Iterable

from zshstats.types import ZshHstRow


def filter_valid_rows(iterable: Iterable) -> Iterator:
    """
    For this program, we're only interested in rows that begin with a colon.
    """
    return (
        row for row in iterable if row[0] == ':'
    )


def filter_not_sudo(iterable: Iterable[ZshHstRow]) -> Iterator[ZshHstRow]:
    return (
        row for row in iterable if row.sudo_cmd is None
    )


def filter_sudo(iterable: Iterable[ZshHstRow]) -> Iterator[ZshHstRow]:
    return (
        row for row in iterable if row.sudo_cmd is not None
    )


def filter_date_range(
        iterable: Iterable[ZshHstRow],
        start: datetime.date,
        end: datetime.date
) -> Iterator[ZshHstRow]:
    return (
        row for row in iterable
        if start <= row.datetime.date() < end
    )


def filter_cmd(iterable: Iterable[ZshHstRow], cmd: str) -> Iterator[ZshHstRow]:
    return (
        row for row in iterable if row.cmd == cmd
    )
