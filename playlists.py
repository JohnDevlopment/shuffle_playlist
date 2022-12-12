"""Module for writing playlists."""

from typing import Protocol

class Playlist(Protocol):
    """Protocol for writing playlists to file."""

    @property
    def string(self) -> str:
        return ""

class M3UPlaylist:
    """Represents a M3u playlist format."""

    def __init__(self, items: list):
        pass

    @property
    def string(self) -> str:
        """Formatted M3U playlist text."""
        return ""

def write_playlist(pl: Playlist, filename: str):
    """Write PL to FILENAME."""
    with open(filename, 'wt') as fd:
        fd.write(pl.string)
