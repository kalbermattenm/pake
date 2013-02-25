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

* pake gives you the full power of Python to script your build actions.  For example, you can use exceptions to gracefully handle errors and clean up temporary files when an action fails.


Example
-------

This example demonstrates most of pake's features.  You can find it in the `examples/simple` directory where you can run it with the command `./build.py`.  To clean up, run `./build.py -c`.

```python
#!/usr/bin/env python

from pake import Target, main, rule, target, variables, virtual

# Variables can be overridden on the command line or with environment
# variables.
variables.CC = 'gcc'

# Normal Python constants can be used
SRC = 'hello.c'

# Virtual targets are like make's .PHONY targets.
virtual('all', 'hello')


# Normal targets consist of the target followed by a list of dependencies,
# the decorated function is the action to build the target.
@target('hello', 'hello.o')
def hello(t):
    t.run('%(CC)s', '-o', t.name, t.dependencies)


# Rules match on regular expressions and return a target.  The decorated
# function receives the target name and the regexp match result and returns a
# new target.
@rule(r'(?P<filename>.*)\.o\Z')
def o(name, match):
    def action(t):
        t.run('%(CC)s', '-c', '-o', t.name, t.dependencies)
    dependencies = '%(filename)s.c' % match.groupdict()
    return Target(name, action=action, dependencies=dependencies)


# Don't forget to call main()!
main()
```

For a more complete examples, see [build.py for OpenLayers 3](https://github.com/openlayers/ol3/blob/master/build.py) and the [equivalent (now outdated) Makefile](https://github.com/openlayers/ol3/blob/5fb39ff30dd27ab0e13c2b468c3feb69789ed4ed/Makefile).


Generating dependency graphs
----------------------------

pake can generate dependency graphs automatically in Dot format, just pass the ``-g`` option.  For example, the dependency graph for the above example is:

```
digraph "all" {
	"all" -> "hello";
	"hello" -> "hello.o";
	"hello.o" -> "hello.c";
}
```
