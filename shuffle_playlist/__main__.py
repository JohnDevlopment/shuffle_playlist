#!/usr/bin/env python3

from argparse import ArgumentParser
from pathlib import Path
from .utils import *
from .playlists import get_playlist as pl_get_playlist, write_playlist as pl_write_playlist

def main():
    # Main function.
    parser = ArgumentParser(prog='shuffle_playlist')
    parser.add_argument('-t', '--title', help='set the title of the playlist')
    parser.add_argument('OUTPUT', type=Path, help='file to write playlist to')
    parser.add_argument('FILE', nargs='+', type=Path,
                        help='files to add to playlist')

    args = parser.parse_args()

    # Gather entry list
    files: list[Path] = args.FILE
    output: Path = args.OUTPUT

    PlaylistClass = pl_get_playlist(output)
    playlist = PlaylistClass(shuffle_list(files), title=args.title)

    print(playlist.get_string())

if __name__ == "__main__":
    main()
