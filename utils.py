# Utility functions
import subprocess, re

_mplayercmd = ('mplayer', '-identify', '-frames', '0')
_id_re = re.compile(r'ID_([A-Z_]+)=(.+)')

class CommandlineError(RuntimeError):
    pass

class StringInputError(RuntimeError):
    pass

def get_named_ids(s: str, *ids) -> dict:
    fields = {}
    for m in _id_re.finditer(s):
        name, value = m.group(1, 2)
        if name.lower() in ids:
            fields[name.lower()] = value
    return fields

def shuffle_list(entries: list):
    import random
    random.shuffle(entries)
    return entries

def read_file_dict(file: str):
    cmd = _mplayercmd + (file,)
    cp = subprocess.run(cmd, capture_output=True, text=True)
    fields = get_named_ids(cp.stdout, 'length', 'aid_0_name', 'filename', 'artist')
    return fields
