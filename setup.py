#!/usr/bin/env python3
from pathlib import Path
from setuptools import setup

"""
def get_version() -> str:
    import ast

    version: str = ""

    source: str = (ROOT / 'shuffle_playlist' / '__init__.py').read_text()

    tree: ast.Module = ast.parse(source)
    for stmt in tree.body:
        if isinstance(stmt, ast.Assign):
            target: ast.Name = cast(ast.Name, stmt.targets[0])
            if target.id == '__version__':
                print(ast.dump(stmt))
                value: ast.Constant = cast(ast.Constant, stmt.value)
                version = value.value
                break

    return version
"""

def get_short_description() -> str:
    import io

    with io.StringIO(LONGDESCRIPTION) as fd:
        fd.readline()
        return fd.readline()

ROOT = Path(__file__).resolve().parent
LONGDESCRIPTION = (ROOT / 'README.md').read_text()

setup(
    python_requires=">=3.8"
)
