# Compile and pack shuffle-playlist.py

from setuptools import setup, find_packages

setup(
    name = 'shuffle_playlist',
    version = '0.2',
    description = 'Creates a shuffled playlist',
    packages = find_packages(),
    py_modules = ['audio', 'utils', 'shuffle_playlist'],
    entry_points = {
        'console_scripts': ['shuffle_playlist = shuffle_playlist:main']
    }
)
