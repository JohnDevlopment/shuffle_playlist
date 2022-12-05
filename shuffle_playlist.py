#!/usr/bin/env python3

from tkinter import Tk, Listbox, StringVar, ttk
from exwidgets.entry import ExEntry
from exwidgets.constants import *
from pathlib import Path
from utils import *
import subprocess, sys, re, meta

Root = Tk()

def write_playlist(files: list, title, output):
    """Writes the playlist to file."""
    # Params
    # Title
    title = title.get()
    if len(title) == 0 or title.isspace():
        raise StringInputError("Title is empty")
    # Output file
    output = output.get()
    if len(output) == 0 or output.isspace() or not output.endswith('.m3u'):
        raise StringInputError("Output file is empty or lacks the .m3u extension")

    # No file arguments
    if len(files) == 0:
        raise CommandlineError("No files were provided")

    entries = []
    artistsep_re = re.compile(r'\s*-\s*')

    def _process(d: dict):
        d['length'] = round(float(d['length']))
        d['title'] = d.get('aid_0_name',
                           artistsep_re.sub(': ', path.with_suffix('').name))
        d['filename'] = d['filename'].replace(' ', '%20')
        return d

    # Gather data from files
    for path in files:
        fields = read_file_dict(str(path))
        entries.append(_process(fields))

    entries = shuffle_list(entries)

    # Write playlist data to file
    with open(output, 'wt') as fd:
        fd.write(f"#EXTM3U\n#PLAYLIST:{title}\n")
        for entry in entries:
            entry.update(meta.read_file(entry['filename'].replace('%20', ' ')))
            artist = entry.get('artist')
            entry['artist'] = f"{artist} - " if artist is not None else ''
            fd.write("#EXTINF:{length},{artist}{title}\n{filename}\n".format(**entry))

    Root.destroy()

def interface():
    Root.title('Create Playlist')

    subframe = ttk.Frame()
    subframe.pack(fill=BOTH)

    files = []
    temp = sys.argv[1:]
    for file in temp:
        file = Path(file)
        file = file.resolve(True)
        if file.exists():
            files.append(file)
    del temp

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

interface()
Root.mainloop()
