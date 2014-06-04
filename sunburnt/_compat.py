import sys

__all__ = ['PY2', 'text_type', 'str_type', 'range_type', 'long_type', 'stringio_type', 'urllib_type', 'urlparse_type', 'reduce_func', 'slice_type']

PY2 = sys.version_info[0] == 2

if PY2:
    range_type = xrange
    text_type = unicode
    long_type = long
    str_type = basestring
    import cStringIO as stringio_type
    import urllib as urllib_type
    import urlparse as urlparse_type
    from types import SliceType as slice_type
    reduce_func = reduce
else:
    range_type = range
    text_type = str
    long_type = int
    str_type = str
    import io  as stringio_type
    from urllib import parse as urllib_type
    from urllib import parse as urlparse_type
    from functools import reduce as reduce_func
    slice_type = slice
