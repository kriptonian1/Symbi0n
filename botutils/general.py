import asyncio
import sys
import traceback
from discord.utils import maybe_coroutine


class CallFromList(list):
    def call(self, *args, **kwargs):
        return asyncio.gather(*(maybe_coroutine(func, *args, **kwargs) for func in self))

def call(func, *args, exception=Exception, ret=False, **kwargs):

    try:
        return func(*args, **kwargs)
    except Exception as err:
        return (None, err)[ret]

def print_error(text, error, *, _print=True):
    """Print Exception with traceback."""

    if _print:
        print(text, file=sys.stderr)
    
    traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)
    err_type = type(error)
    trace = error.__traceback__
    lines = traceback.format_exception(err_type, error, trace)
    return "".join(lines)