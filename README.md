pake
====

A simple implementation of make in pure Python with no external dependencies


Why use pake?
-------------

* pake allows you to replace your Makefiles with a single platform-independent build script with no external dependencies except Python.  You can use the same build script on Linux, Mac OS X, Windows, and more.

* pake is contained in a single, short Python file which is trivially easy to distribute: just copy it into your project.

* pake is a generic build tool, just like make, it can be used for building projects written in any language.

* pake's declarative pure-Python DSL will be instantly familiar to developers familiar with make.

* pake uses timestamps to determine when to rebuild targets, just like make.

* pake is fast. As many tasks can be accomplished in pure Python, without spawning a subprocess, pake is faster than make.

* pake supports normal targets, virtual targets, variables, and rules.

* pake automatically creates 'clean' targets for you, just pass the `-c` option.

* pake exposes its underlying data model so you can easily script it for custom build logic.


Example
-------

This example demonstrates most of pake's features.  You can find it in the `example` directory where you can run it with the command `./build.py`.  To clean up, run `./build -c`.

```python
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
```

For a more complete examples, see [build.py for ol3](https://github.com/twpayne/ol3/blob/pure-python-build/build.py) and the [equivalent Makefile](https://github.com/twpayne/ol3/blob/pure-python-build/Makefile).
