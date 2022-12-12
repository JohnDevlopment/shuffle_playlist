"""
Utility functions and classes.

Functions:
    * shuffle_playlist()
"""

from typing import Protocol, Union, runtime_checkable
import random

class CommandlineError(RuntimeError):
    pass

class StringInputError(RuntimeError):
    pass

def shuffle_list(values: list) -> list:
    """Shuffles the items in a list."""
    random.shuffle(values)
    return values
