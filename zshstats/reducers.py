from collections import Counter
from typing import Iterator, Iterable

from zshstats.types import ZshHstRow, ZshHstCmdCount
from zshstats.utils import second


def count_cmds(iterable: Iterable[ZshHstRow], cmd_key: str) -> Iterator[ZshHstCmdCount]:
    """Reduces the provided """
    sorted_counts = sorted(
        Counter(getattr(row, cmd_key) for row in iterable).items(),
        key=lambda x: second(x), reverse=True
    )

    return (
        ZshHstCmdCount(cmd=cmd, count=cnt)
        for cmd, cnt in sorted_counts
    )
