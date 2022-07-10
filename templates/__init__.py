"""
Templates
~~~~~~~~~~~~~~~~~

A utility for creating dynamic project templates.

"""

__title__: str = "Templates"
__author__: str = "nicdgonzalez"
__license__: str = "Apache-2.0"
__copyright__: str = "Copyright (c) 2022-present " + __author__
__version__: str = "0.1.0"
__repository__: str = "https://github.com/nicdgonzalez/Templates"

from typing import NamedTuple

# from .module_name import *


class VersionInfo(NamedTuple):
    major: int
    minor: int
    patch: int


version_info: VersionInfo = VersionInfo(*__version__.split(".", maxsplit=3))

del VersionInfo, NamedTuple
