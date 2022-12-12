"""
Utility functions and classes.

Functions:
    * shuffle_playlist()
"""

from typing import Protocol, Union
import random

class CommandlineError(RuntimeError):
    pass

class StringInputError(RuntimeError):
    pass

class FileDescriptor(Protocol):
    """Describes a file descriptor."""

    def write(self, data: Union[str, bytes]):
        """Write DATA to file."""

def shuffle_list(values: list) -> list:
    """Shuffles the items in a list."""
    random.shuffle(values)
    return values
