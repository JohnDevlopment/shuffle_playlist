# Compile and pack shuffle-playlist.py

from setuptools import setup, find_packages

print(find_packages())

setup(
    name = 'shuffle_playlist',
    version = '0.1',
    description = 'Creates a shuffled playlist',
    packages = find_packages(),
    py_modules = ['meta', 'utils', 'shuffle_playlist'],
    entry_points = {
        'console_scripts': ['shuffle_playlist = shuffle_playlist:main']
    }
)
