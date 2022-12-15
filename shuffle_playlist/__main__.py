#!/usr/bin/env python3

from argparse import ArgumentParser, Namespace
from pathlib import Path
from typing import Any
from dataclasses import dataclass
from .utils import *
from .playlists import get_playlist as pl_get_playlist

__all__ = ['Parameters', 'parse_commandline', 'main']

@dataclass
class Parameters:
    files: list[Path]
    output: Path | str
    format_: str
    args: Namespace

def parse_commandline(*_argv: str):
    parser = ArgumentParser(prog='shuffle_playlist', description="A tool for creating shuffled playlists")
    parser.add_argument('-t', '--title', help='set the title of the playlist')
    parser.add_argument('-f', '--format', help='playlist format')
    parser.add_argument('OUTPUT', help='file to write playlist to')
    parser.add_argument('FILE', nargs='+', type=Path,
                        help='files to add to playlist')

    args = parser.parse_args(_argv)

    files: list[Path] = args.FILE
    output: Path | str = args.OUTPUT

    # If output is '-', then --format is required
    ext: Any = None
    if output == '-':
        ext = args.format
        if ext is None:
            raise CommandlineError("missing '--format' option: required when OUTPUT is '-'",
                                   user_data=parser)
    else:
        output = Path(output).resolve()
        ext = args.format or get_file_extension(output)

    args.extension = ext

    return Parameters(files=files, output=output, args=args, format_=ext)

def main():
    # Main function.
    params = parse_commandline()
    args = params.args

    ext = args.extension
    files = params.files
    output = params.output

    PlaylistClass = pl_get_playlist(ext)
    playlist = PlaylistClass(shuffle_list(files), title=args.title)

    if output == '-':
        print(playlist.get_string())

if __name__ == "__main__":
    main()
