# Utility functions
import random

class CommandlineError(RuntimeError):
    pass

class StringInputError(RuntimeError):
    pass

def shuffle_list(entries: list):
    random.shuffle(entries)
    return entries
