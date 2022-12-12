"""Module for writing playlists."""

from typing import Protocol, Union
from dataclasses import dataclass
from abc import ABC, abstractmethod
from pathlib import Path
import re, audio

class Playlist(Protocol):
    """Protocol for writing playlists to file."""

    @property
    def string(self) -> str:
        return ""

class PlaylistEntry(ABC):
    """Abstract class representing an entry in a playlist."""

    def __init__(self, p: Path):
        self.filename: str = str(p)
        self.length: float = 0
        self.tags: dict = {}
        #artistsep_re = re.compile(r'\s*-\s*')
        #artistsep_re.sub(': ', item['title']),
        #round(item['length']),
        #item['filename']

class PlaylistOggEntry(PlaylistEntry):
    """An Ogg Vorbis file playlist entry."""

    def __init__(self, p: Path):
        super().__init__(p)
        tags = audio.get_tags(str(p))
        self.tags = tags.tags.as_dict()

    @property
    def title(self) -> Union[str, None]:
        """"""
        title: str = self.tags.get('title', None)
        return title

class M3UPlaylist:
    """Represents a M3u playlist format."""

    def __init__(self, items: list):
        """
        Construct M3u playlist from ITEMS.

        Each index in ITEMS should be a Path to a file.
        """
        self.entries = [PlaylistOggEntry(item) for item in items]

    @property
    def string(self) -> str:
        """Formatted M3U playlist text."""
        msg = "#EXTM3U\n#PLAYLIST:{title}\n"

        for entry in self.entries:
            artist = entry.tags

        #.replace(' ', '%20')

        #for entry in entries:
        #    entry.update(get_tags(entry['filename'].replace('%20', ' ')))
        #    artist = entry.get('artist')
        #    entry['artist'] = f"{artist} - " if artist is not None else ''
        #    fd.write("#EXTINF:{length},{artist}{title}\n{filename}\n".format(**entry))
        return ""

def write_playlist(pl: Playlist, filename: str):
    """Write PL to FILENAME."""
    with open(filename, 'wt') as fd:
        fd.write(pl.string)
