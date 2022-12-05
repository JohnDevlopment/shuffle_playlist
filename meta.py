# Metadata
from pathlib import Path
import subprocess, re

def read_file(f: str):
    """..."""
    cmdline = ('vorbiscomment', '-l', f)
    cp = subprocess.run(cmdline, capture_output=True, text=True)
    text = cp.stdout

    metadata = {}
    meta_re = re.compile(r'(\w+)=(.+)')
    for m in meta_re.finditer(text):
        key, value = m.group(1, 2)
        metadata[key] = value

    return metadata
