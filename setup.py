import os
from setuptools import setup

README = open(os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'README.rst')).read()

setup(
        name='pake',
        version='0.1',
        description='A simple implementation of make in pure Python',
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development :: Build Tools',
        ],
        author='Tom Payne',
        author_email='twpayne@gmail.com',
        url='https://github.com/twpayne/pake',
        license='BSD',
        zip_safe=True,
        long_description=README,
        )



