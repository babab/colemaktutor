# vim: set et ts=4 sw=4 sts=4 ai:

from distutils.core import setup
import colemaktutor.colemaktutor

long_desc = '''Colemak tutor helps you to learn and practise typing in
the colemak layout (and qwerty layout).

Colemak tutor allows you to emulate a layout so you can learn and
practice typing in colemak without the need for installing an
implementation for your operating system.
'''

setup(
    name='colemaktutor',
    version=colemaktutor.colemaktutor.__version__,
    description=colemaktutor.colemaktutor.__doc__,
    author=colemaktutor.colemaktutor.__author__,
    author_email='benjamin@babab.nl',
    url='http://colemaktutor.babab.nl/',
    download_url='http://pypi.python.org/pypi/DisPass/',
    packages=['colemaktutor'],
    license='ISC',
    long_description=long_desc,
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.4',
        'Topic :: Utilities',
    ],
    scripts=['scripts/colemaktutor'],
    )
