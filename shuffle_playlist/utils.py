"""
Utility functions and classes.

Functions:
    * shuffle_playlist()
"""

from typing import Protocol, Union, overload
import random, re

class CommandlineError(RuntimeError):
    """An error for wrong commandline arguments."""

class StringInputError(RuntimeError):
    """An error for invalid string input."""

class FileDescriptor(Protocol):
    """Describes a file descriptor."""

    def write(self, data: Union[str, bytes]):
        """Write DATA to file."""

_ext_re = re.compile(r'\.(\w+)')

def get_file_extension(_file: str) -> str | None:
    m = _ext_re.search(_file)
    if not m: return None
    return m[1]

def shuffle_list(values: list) -> list:
    """Shuffles the items in a list."""
    random.shuffle(values)
    return values