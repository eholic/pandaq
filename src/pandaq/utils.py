"""Utility functions."""
from __future__ import annotations

import datetime as dt


def join_and(qlist: list[str], *, no_paren=False) -> str:
    """Joins a list of strings with ' & ' and optionally wraps them in parentheses.

    Args:
        qlist: A list of strings to be joined.
        no_paren: If True, the joined string is not wrapped in parentheses. Defaults to False.

    Returns:
        The joined string.
    """
    text = " & ".join(qlist)
    if len(qlist) == 1 or no_paren:
        return text
    else:
        return f"({text})"


def join_or(qlist: list[str], *, no_paren=False) -> str:
    """Joins a list of strings with ' | ' and optionally wraps them in parentheses.

    Args:
        qlist (list): A list of strings to be joined.
        no_paren (bool, optional): If True, the joined string is not wrapped in parentheses. Defaults to False.

    Returns:
        The joined string.
    """
    text = " | ".join(qlist)
    if len(qlist) == 1 or no_paren:
        return text
    else:
        return f"({text})"


def dtime_to_str(dtime: dt.date | dt.datetime) -> str:
    """Converts a datetime object to a string.

    Args:
        dtime: The datetime object to be converted.

    Returns:
        The datetime as a string.
    """
    if isinstance(dtime, dt.datetime):
        fmt = "%Y-%m-%d %H:%M:%S"
        if dtime.microsecond > 0:
            fmt += ".%f"
        text = dtime.strftime(fmt)
    elif isinstance(dtime, dt.date):
        text = dtime.strftime("%Y-%m-%d")
    else:
        msg = f"Unsupported type {type(dtime)} for dtime."
        raise TypeError(msg)
    return f'"{text}"'
