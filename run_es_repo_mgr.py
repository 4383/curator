#!/usr/bin/env python

"""
Wrapper for running es_repo_mgr from source.

When used with Python 3 (and the DEB and RPM packages of Curator are compiled
and bundled with Python 3), Curator requires the locale to be unicode. Any of
the above unicode definitions are acceptable.

To set the locale to be unicode, try:

$ export LC_ALL=en_US.utf8
$ es_repo_mgr [ARGS]

Alternately, you should be able to specify the locale on the command-line:

$ LC_ALL=en_US.utf8 es_repo_mgr [ARGS]

Be sure to substitute your unicode variant for en_US.utf8

"""

from curator.bin.run import main, EXE


if __name__ == '__main__':
    main(EXE.repomgrcli, __doc__)
