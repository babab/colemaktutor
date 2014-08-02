#!/usr/bin/env python3

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
    from colors import (
        # red,
        # green,
        # magenta,
        # cyan,
        # underline,
        bold,
    )
except ImportError:
    bold = lambda x: x

from lessons import ColemakLessons
from tutor import CLITutor
import cli


class KeyMapper:
    layout_in = 'qwerty'
    layout_out = 'colemak'

    Q = 'qwertyuiopasdfghjkl;zxcvbnm'  # QWERTY
    C = 'qwfpgjluy;arstdhneiozxcvbkm'  # COLEMAK

    def config(self, layout_tuple):
        self.layout_in = layout_tuple[0]
        self.layout_out = layout_tuple[1]
        return self

    def get(self, key):
        if self.layout_in == 'qwerty' and self.layout_out == 'colemak':
            return self.C[self.Q.find(key)] if key in self.Q else key
        elif self.layout_in == 'colemak' and self.layout_out == 'qwerty':
            return self.Q[self.C.find(key)] if key in self.C else key
        return key


def header():
    os.system('cls' if os.name == 'nt' else 'clear')
    div = lambda x: ((' ' * x) + '---' + (' ' * x))
    print(bold(versionStr) + div(14) + 'http://colemak-tutor.babab.nl')
    print(('=' * 80) + '\n')


def main():
    header()
    mapper = KeyMapper()
    mapper.config(cli.layout())
    tutor = CLITutor(mapper)

    if mapper.layout_out == 'colemak':
        ColemakLessons(tutor, header_func=header, start=1)
    else:
        print('That is not available yet, please select another option')
        input('--- Press enter ---')
        main()

if __name__ == "__main__":
    main()
