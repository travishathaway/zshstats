from typing import Iterator, Iterable

from zshstats.types import ZshHstCmdCount


def format_leading_number(iterable: Iterable[ZshHstCmdCount]) -> Iterator[str]:
    """
    Adds leading sequencial numbers to sequence
    """
    return (
        f'{idx}. {row.cmd}: {row.count}'
        for idx, row in enumerate(iterable, start=1)
    )
