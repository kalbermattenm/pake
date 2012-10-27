#!/usr/bin/env python

import pake

pake.variables['CC'] = 'gcc'

SRC = 'hello.c'

pake.virtual('all', 'hello')

@pake.target('hello', 'hello.o')
def hello(t):
    t.run(pake.variables['CC'], '-o', t.name, t.dependencies)

@pake.rule(r'(?P<filename>.*)\.o\Z')
def o(name, match):
    def action(t):
        t.run(pake.variables['CC'], '-c', '-o', t.name, t.dependencies)
    dependencies = '%(filename)s.c' % match.groupdict()
    return pake.Target(name, action=action, dependencies=dependencies)       

pake.main()
