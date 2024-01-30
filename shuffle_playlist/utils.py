"""
Utility functions and classes.

Functions:
    * get_file_extension()
    * shuffle_playlist()
"""

from typing import Protocol, Optional, cast
from pathlib import Path
import random, re

class CommandlineError(RuntimeError):
    """
    An error for wrong commandline arguments.

    USER_DATA can be used to provide user data, which
    the user can.
    """

    def __init__(self, *args, user_data=None, **kw):
        self.user_data = user_data
        super().__init__(*args, **kw)

class StringInputError(RuntimeError):
    """An error for invalid string input."""

class FileDescriptor(Protocol):
    """Describes a file descriptor."""

    def write(self, data: str | bytes):
        """Write DATA to file."""

_ext_re = re.compile(r'\.(\w+)')

def get_file_extension(_file: Path | str) -> Optional[str]:
    """
    Get the extension of _FILE.

    Returns a string unless _FILE is a string and there is
    not extension, in which case it returns None.
    """
    if isinstance(_file, Path):
        pfile = cast(Path, _file)
        res = str(pfile.suffix)
        return res[1:] or None
    elif (_file, str):
        sfile = cast(str, _file)
        m = _ext_re.search(sfile)
        return m[1] if m else None

def shuffle_list(values: list) -> list:
    """Shuffles the items in a list."""
    random.shuffle(values)
    return values

__all__ = [
    # Classes
    'CommandlineError',
    'FileDescriptor',
    'StringInputError',

    # Functions
    'get_file_extension',
    'shuffle_list'
]
