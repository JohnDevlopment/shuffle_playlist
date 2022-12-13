from ..playlists import get_playlist, M3UPlaylist, PlaylistEntry
from pytest import fixture, MonkeyPatch
from typing import no_type_check, cast
from pathlib import Path
import pytest, os, dotenv

env = dotenv.find_dotenv()
if env:
    dotenv.load_dotenv(env)
del env

@fixture
def files() -> list[Path] | None:
    string = os.getenv('PYTEST_PL_FILES')
    if string is None: return None

    files: list[Path] = list()

    # Character used to separate
    sep = string[0]
    string = string[1:]

    # Split string into list
    for _file in string.split(sep):
        path = Path(_file).resolve()
        if path.exists():
            files.append(path)

    return files

class MockOggTags:
    pass

class MockOggEntry(PlaylistEntry):
    def __init__(self, p: Path):
        super().__init__(p)
        tags = 0

    def get_format(self) -> str:
        return "Ogg Vorbis"

class TestPlaylistTypes:
    @no_type_check
    def test_m3u_playlist(self, files, capsys):
        def mock_get_tags():
            pass

        print("set PYTEST_PL_FILES to a list absolute paths to files to process"
              ", separated by the first character in the string.\n"
              "Example: :file1.ogg:file2.wav")
        assert files is not None

        pl = M3UPlaylist(files)

        with capsys.disabled():
            print(pl.get_string())
