#!/usr/bin/env python

from pake import ifind, main, target, virtual


SRC = [path for path in ifind('.') if path.endswith('.py')]


virtual('all', 'pep8', 'pyflakes')


@target('pep8', SRC, phony=True)
def pep8(t):
    t.run('pep8', SRC)


@target('pyflakes', SRC, phony=True)
def pyflakes(t):
    t.run('pyflakes', SRC)


if __name__ == '__main__':
    main()
