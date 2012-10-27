#!/usr/bin/env python

import pake


SRC = 'pake.py'


pake.virtual('all', 'pep8', 'pyflakes')


@pake.target('pep8', SRC, phony=True)
def pep8(t):
    t.run('pep8', SRC)


@pake.target('pyflakes', SRC, phony=True)
def pep8(t):
    t.run('pyflakes', SRC)


if __name__ == '__main__':
    pake.main()
