"""utils."""
from __future__ import annotations

import datetime as dt


def join_and(qlist: list, *, no_paren=False) -> str:
    text = " & ".join(qlist)
    if len(qlist) == 1 or no_paren:
        return text
    else:
        return f"({text})"


def join_or(qlist: list, *, no_paren=False) -> str:
    text = " | ".join(qlist)
    if len(qlist) == 1 or no_paren:
        return text
    else:
        return f"({text})"


def dtime_to_str(dtime: dt.date|dt.datetime) -> str:
    if isinstance(dtime, dt.datetime):
        fmt = "%Y-%m-%d %H:%M:%S"
        if dtime.microsecond > 0:
            fmt += ".%f"
        text = dtime.strftime(fmt)

    else:
        text = dtime.strftime("%Y-%m-%d")
    return f'"{text}"'
