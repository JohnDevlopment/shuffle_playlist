"""Audio functions and classes."""

from soundfile import SoundFile
from mutagen.oggvorbis import OggVorbis
from pathlib import PurePath

class ExSoundFile(SoundFile):
    @property
    def seconds(self) -> float:
        """Length in seconds."""
        return float(self.frames * self.channels) / float(self.samplerate)

def get_tags(filename: str) -> OggVorbis:
    """Get meta tags for the given FILENAME."""
    return OggVorbis(filename)

def get_file_dict(filename: str) -> dict:
    """
    Return a dictionary with information about FILENAME.

    The returned dictionary contains the following:
        * length (float) - the length of the song in seconds
        * title (str, None) - the title of the song, or None if unavailable
        * filename (str) - the name of the file with the leading path removed
    """
    ogg = ExSoundFile(filename)
    res = {
        'length': ogg.seconds,
        'filename': ogg.name,
        'title': None
    }
    oggtags = get_tags(filename)

    # Get title
    try:
        title = oggtags['title']
    except:
        temp = PurePath(res['filename']).stem
        title = str(temp)

    if isinstance(title, list):
        title = ' '.join(title)

    res['title'] = title

    return res
