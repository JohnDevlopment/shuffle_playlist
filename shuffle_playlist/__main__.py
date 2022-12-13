#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
from .utils import *
from .playlists import get_playlist as pl_get_playlist, write_playlist as pl_write_playlist
import sys

"""
def write_playlist(files: list, **kw):
    # Params
     # Title
    title: str = titleVar.get()
    if len(title) == 0 or title.isspace():
        raise StringInputError("Title is empty")

     # Output file
    output: str = outputVar.get()
    if len(output) == 0 or output.isspace() or not output.endswith('.m3u'):
        raise StringInputError("Output file is empty or lacks the .m3u extension")

    # Gather entry list
    PlaylistClass = pl_get_playlist(output)
    playlist = PlaylistClass(shuffle_list(files))
    pl_write_playlist(playlist, output)

    Root.destroy()
"""

def main():
    # Main function.
    parser = ArgumentParser(prog='shuffle_playlist')
    parser.add_argument('-t', '--title', help='')
    parser.add_argument('OUTPUT', type=Path, help='file to write playlist to')
    parser.add_argument('FILE', nargs='+', type=Path,
                        help='files to add to playlist')

    args = parser.parse_args()

    # Gather entry list
    files: list[Path] = args.FILE
    output: Path = args.OUTPUT

    PlaylistClass = pl_get_playlist(output)
    playlist = PlaylistClass(shuffle_list(files))

    print(playlist.get_string())

if __name__ == "__main__":
    main()
