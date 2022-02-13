from datetime import datetime
from typing import NamedTuple, Optional


class ZshHstRow(NamedTuple):
    datetime: Optional[datetime]
    cmd: Optional[str]
    args: Optional[tuple[str]]
    sudo_cmd: Optional[str]


class ZshHstCmdCount(NamedTuple):
    cmd: str
    count: int
