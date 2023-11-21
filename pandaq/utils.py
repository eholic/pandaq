"""utils."""
import datetime as dt

from typing import Union


def join_and(qlist: list, no_paren=False) -> str:
    text = " & ".join(qlist)
    if len(qlist) == 1 or no_paren:
        return text
    else:
        return f"({text})"


def join_or(qlist: list, no_paren=False) -> str:
    text = " | ".join(qlist)
    if len(qlist) == 1 or no_paren:
        return text
    else:
        return f"({text})"


def dtime_to_str(dtime: Union[dt.date, dt.datetime]) -> str:
    if isinstance(dtime, dt.datetime):
        format = "%Y-%m-%d %H:%M:%S"
        if dtime.microsecond > 0:
            format += ".%f"
        text = dtime.strftime(format)

    else:
        text = dtime.strftime("%Y-%m-%d")
    return f'"{text}"'
