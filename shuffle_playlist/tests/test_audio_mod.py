from ..audio import _ext_re, get_tags
from mutagen._util import MutagenError
import pytest, os

@pytest.fixture(scope="class")
def re_valid_match():
    fn = os.getenv('PYTEST_FILENAME') or 'file.ogg'
    return _ext_re.search(fn)

class TestRegex:
    def test_regex(self, capsys):
        with capsys.disabled():
            print("Add regular express:", _ext_re)
        assert _ext_re is not None

    def test_regex_on_string(self, re_valid_match):
        assert re_valid_match is not None

    def test_regex_get_group1(self, re_valid_match, capsys):
        assert re_valid_match is not None
        ext = re_valid_match[1]
        with capsys.disabled():
            print("Extension:", ext)
        assert ext == 'ogg'

@pytest.fixture(scope="class")
def filename() -> str:
    return os.getenv('PYTEST_FILENAME') or 'file.ogg'

class TestTagParsers:
    @staticmethod
    def get_tags(filename: str):
        try:
            tags = get_tags(filename)
        except MutagenError as exc:
            msg = str(exc) + "set PYTEST_FILENAME to an existing file"
            raise RuntimeError(msg)

        return tags

    def test_ogg_tags(self, filename: str):
        from ..audio import OggTagParser
        try:
            print(f"tried to open {filename}")
            tags = OggTagParser(filename)
        except MutagenError as exc:
            msg = str(exc) + ": set PYTEST_FILENAME to an existing file"
            raise RuntimeError(msg)

    def test_get_tags(self, filename: str, capsys):
        tags = self.get_tags(filename)
        assert tags is not None
        assert hasattr(tags, "get_tags")
        assert hasattr(tags, "get_info")

        with capsys.disabled():
            temp = tags.get_tags()
            print('tags:')
            for k, v in temp.items():
                print(f"\t{k} = {v}")

            temp = tags.get_info()
            print('file info:')
            for k, v in temp.items():
                print(f"\t{k} = {v}")
