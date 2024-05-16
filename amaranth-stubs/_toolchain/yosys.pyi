"""
This type stub file was generated by pyright.
"""

__all__ = ["YosysError", "YosysBinary", "find_yosys"]
from typing import Optional
from pathlib import Path


class YosysError(Exception):
    ...


class YosysWarning(Warning):
    ...


class YosysBinary:
    @classmethod
    def available(cls) -> bool:
        """Check for Yosys availability.

        Returns
        -------
        available : bool
            ``True`` if Yosys is installed, ``False`` otherwise. Installed binary may still not
            be runnable, or might be too old to be useful.
        """
        ...
    
    @classmethod
    def version(cls) -> Optional[tuple[int, int, int]]:
        """Get Yosys version.

        Returns
        -------
        ``None`` if version number could not be determined, or a 3-tuple ``(major, minor, distance)`` if it could.

        major : int
            Major version.
        minor : int
            Minor version.
        distance : int
            Distance to last tag per ``git describe``. May not be exact for system Yosys.
        """
        ...
    
    @classmethod
    def data_dir(cls) -> Path:
        """Get Yosys data directory.

        Returns
        -------
        data_dir : pathlib.Path
            Yosys data directory (also known as "datdir").
        """
        ...
    
    @classmethod
    def run(cls, args: list[str], stdin: str=...) -> str:
        """Run Yosys process.

        Parameters
        ----------
        args : list of str
            Arguments, not including the program name.
        stdin : str
            Standard input.

        Returns
        -------
        stdout : str
            Standard output.

        Exceptions
        ----------
        YosysError
            Raised if Yosys returns a non-zero code. The exception message is the standard error
            output.
        """
        ...
    


class _BuiltinYosys(YosysBinary):
    YOSYS_PACKAGE = ...
    @classmethod
    def available(cls): # -> bool:
        ...
    
    @classmethod
    def version(cls): # -> tuple[int, int, int]:
        ...
    
    @classmethod
    def data_dir(cls): # -> Traversable:
        ...
    
    @classmethod
    def run(cls, args, stdin=..., *, ignore_warnings=..., src_loc_at=...):
        ...
    


class _SystemYosys(YosysBinary):
    YOSYS_BINARY = ...
    @classmethod
    def available(cls) -> bool:
        ...
    
    @classmethod
    def version(cls): # -> tuple[int, int, int] | None:
        ...
    
    @classmethod
    def data_dir(cls) -> Path:
        ...
    
    @classmethod
    def run(cls, args, stdin=..., *, ignore_warnings=..., src_loc_at=...):
        ...
    


def find_yosys(requirement):
    """Find an available Yosys executable of required version.

    Parameters
    ----------
    requirement : function
        Version check. Should return ``True`` if the version is acceptable, ``False`` otherwise.

    Returns
    -------
    yosys_binary : subclass of YosysBinary
        Proxy for running the requested version of Yosys.

    Exceptions
    ----------
    YosysError
        Raised if required Yosys version is not found.
    """
    ...

