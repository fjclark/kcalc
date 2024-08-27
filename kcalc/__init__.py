"""Tutorial"""

from . import _version

__all__ = ["calc_k"]

from .conversion import calc_k

__version__ = _version.get_versions()["version"]
__all__ = ["__version__"]
