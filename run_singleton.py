#!/usr/bin/env python

"""
Wrapper for running singletons from source.

When used with Python 3 (and the DEB and RPM packages of Curator are compiled
and bundled with Python 3), Curator requires the locale to be unicode. Any of
the above unicode definitions are acceptable.

To set the locale to be unicode, try:

$ export LC_ALL=en_US.utf8
$ curator_cli [ARGS]

Alternately, you should be able to specify the locale on the command-line:

$ LC_ALL=en_US.utf8 curator_cli [ARGS]

Be sure to substitute your unicode variant for en_US.utf8

"""

from curator.run import run, EXE


if __name__ == '__main__':
    run(
        EXE.singletoncli,
        __doc__
    )
