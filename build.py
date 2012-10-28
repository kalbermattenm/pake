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


@pake.target('pypi-upload', 'all', phony=True)
def pypi_upload(t):
    t.run('python', 'setup.py', 'sdist', 'upload')


if __name__ == '__main__':
    pake.main()
