#!/usr/bin/env python3

'''Main program module for all interfaces

This is the main module but really does nothing more then definining
meta information. Look at cli.CLI.main() for the main program, which is
command line only at the moment.
'''

# Copyright (c) 2014 Benjamin Althues <benjamin@babab.nl>
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

__docformat__ = 'restructuredtext'
__author__ = "Benjamin Althues"
__copyright__ = "Copyright (C) 2014  Benjamin Althues"
__version_info__ = (0, 1, 0, 'alpha', 0)
__version__ = '0.1.0'
versionStr = 'colemak-tutor ' + __version__

import os

try:
    from colors import bold
except ImportError:
    bold = lambda x: x

from lessons import ColemakLessons
from tutor import CLITutor
import cli


class KeyMapper:
    '''Map keys between the Colemak and Qwerty layouts'''

    layout_in = 'qwerty'
    '''A string describing the input layout. Can be 'colemak' or 'qwerty' '''

    layout_out = 'colemak'
    '''A string describing the output layout. Can be 'colemak' or 'qwerty' '''

    Q = 'qwertyuiopasdfghjkl;zxcvbnm'
    '''Key sequence for the 'qwerty' layout'''

    C = 'qwfpgjluy;arstdhneiozxcvbkm'
    '''Key sequence for the 'colemak' layout'''

    def config(self, layout_tuple):
        '''Setter method for the `layout_in` and `layout_out` properties'''
        self.layout_in = layout_tuple[0]
        self.layout_out = layout_tuple[1]
        return self

    def get(self, key):
        '''Get a key depending on settings'''
        if self.layout_in == 'qwerty' and self.layout_out == 'colemak':
            return self.C[self.Q.find(key)] if key in self.Q else key
        elif self.layout_in == 'colemak' and self.layout_out == 'qwerty':
            return self.Q[self.C.find(key)] if key in self.C else key
        return key


def header(mapper=None):
    '''Clear the terminal screen and print the program header'''
    os.system('cls' if os.name == 'nt' else 'clear')
    print(('=' * 80))
    div = lambda x: ((' ' * x) + '---' + (' ' * x))
    print(bold(versionStr) + div(14) + 'http://colemak-tutor.babab.nl')

    if mapper:
        print('\nkeyboard layout: in = {in_} / out = {out}'
              .format(in_=mapper.layout_in, out=mapper.layout_out))
    print(('=' * 80) + '\n')


def main():
    '''Main function for running colemaktutor's interactive CLI'''
    header()
    mapper = KeyMapper()
    mapper.config(cli.layout())
    tutor = CLITutor(mapper)

    if mapper.layout_out == 'colemak':
        headerf = lambda: header(mapper)
        lessons = ColemakLessons(tutor, header_func=headerf)
        headerf()
        start_with_lesson = cli.selectLesson(lessons.titles)
        lessons.start(start_with_lesson)
    else:
        print('That is not available yet, please select another option')
        input('--- Press enter ---')
        main()

if __name__ == "__main__":
    main()
