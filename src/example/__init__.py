""" A Python demo for SWIG """

from .example import (
    cvar,
    fact,
    get_time,
    my_mod,
)
from .stl_example import (
    Int2strMap,
    Str2intMap,
    echo,
    reverse_map,
    vector_int2str,
)
from ._meta import (
    __author__,
    __email__,
    __url__,
    __copyright__,
    __license__,
    __version__,
)

__all__ = [
    'cvar',
    fact.__name__,
    get_time.__name__,
    my_mod.__name__,
    Int2strMap.__name__,
    Str2intMap.__name__,
    echo.__name__,
    reverse_map.__name__,
    vector_int2str.__name__,
    '__author__',
    '__email__',
    '__url__',
    '__copyright__',
    '__license__',
    '__version__',
]
