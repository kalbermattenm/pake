#!/usr/bin/env python

import pake

# Variables can be overridden on the command line or with environment
# variables.
pake.variables.CC = 'gcc'

# Normal Python constants can be used
SRC = 'hello.c'

# Virtual targets are like make's .PHONY targets.
pake.virtual('all', 'hello')

# Normal targets consist of the target followed by a list of dependencies,
# the decorated function is the action to build the target.
@pake.target('hello', 'hello.o')
def hello(t):
    t.run('%(CC)s', '-o', t.name, t.dependencies)

# Rules match on regular expressions and return a target.  The decorated
# function receives the target name and the regexp match result and returns a
# new target.
@pake.rule(r'(?P<filename>.*)\.o\Z')
def o(name, match):
    def action(t):
        t.run('%(CC)s', '-c', '-o', t.name, t.dependencies)
    dependencies = '%(filename)s.c' % match.groupdict()
    return pake.Target(name, action=action, dependencies=dependencies)       

# Don't forget to call main()!
pake.main()
