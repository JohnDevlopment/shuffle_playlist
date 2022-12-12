#!/usr/bin/env python3

from tkinter import Tk, StringVar, ttk
from exwidgets.entry import ExEntry
from exwidgets.constants import *
from pathlib import Path
from .utils import *
import sys, playlists as pl

def write_playlist(files: list, titleVar: StringVar, outputVar: StringVar):
    """Writes the playlist to file."""
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
    PlaylistClass = pl.get_playlist(Path(output))
    playlist = PlaylistClass(shuffle_list(files))
    pl.write_playlist(playlist, output)

    Root.destroy()

def _check_arguments(files: list):
    # No file arguments
    if len(files) == 0:
        raise CommandlineError("No files were provided")

def interface():
    Root.title('Create Playlist')

    subframe = ttk.Frame()
    subframe.pack(fill=BOTH)

    files = []
    temp = sys.argv[1:]
    for _file in temp:
        _file = Path(_file)
        _file = _file.resolve(True)
        if _file.exists():
            files.append(_file)
    del temp

    _check_arguments(files)

    enTitle = ExEntry(subframe, label='Title', width=100,
                      textvariable=(evar1 := StringVar()))

    enOutput = ExEntry(subframe, label='Output File', width=100,
                       textvariable=(evar2 := StringVar()))
    evar2.set('playlist.m3u')

    button = ttk.Button(subframe, text='Create Playlist',
                        command=lambda: write_playlist(files, evar1, evar2))

    enTitle.pack()
    enOutput.pack()
    button.pack()

    Root.after_idle(lambda: enTitle.focus())

def main():
    global Root
    Root = Tk()
    interface()
    Root.mainloop()

if __name__ == "__main__":
    main()
