"""
{Project}
~~~~~~~~~~~~~~~~~

A brief description about the project.

"""

__title__: str = ""
__author__: str = "nicdgonzalez"
__license__: str = ""
__copyright__: str = "Copyright (c) 2022-present " + __author__
__version__: str = "0.1.0"
__repository__: str = ""

from typing import NamedTuple

# from .module import stuff


class VersionInfo(NamedTuple):
    major: int
    minor: int
    patch: int


version_info: VersionInfo = VersionInfo(*__version__.split(".", maxsplit=3))

del VersionInfo, NamedTuple
