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

import sys
from getch import getch

from colors import (
    red,
    # green,
    # magenta,
    # cyan,
    # underline,
    bold,
)


def write(text='', end='\r'):
    sys.stdout.write((' ' * 80) + '\r' + text + end)
    sys.stdout.flush()


def inputChar(text='', valid_chars=''):
    if text:
        write(text + '\r')

    if not valid_chars:
        return getch

    while True:
        inp = getch()
        if inp in valid_chars:
            write(text + ' ' + inp, end='\n')
            return inp
        wrongtext = red('wrong option')
        write(text + ' ' + wrongtext if text else wrongtext)


def layout():
    print('Colemak tutor allows you to emulate a layout so you can')
    print('learn and practice typing in colemak without installing')
    print('an implementation for your operating system\n')
    print('1 - I want to practise colemak using a qwerty layout (emulated)')
    print('2 - I want to practise colemak using a colemak layout')
    print('3 - I want to practise qwerty using a colemak layout (emulated)')
    print('4 - I want to practise qwerty using a qwerty layout\n')

    inp = inputChar(bold('Select an option:'), '1234')
    if inp == '1':
        return ('qwerty', 'colemak')
    elif inp == '2':
        return ('colemak', 'colemak')
    elif inp == '3':
        return ('colemak', 'qwerty')
    return ('qwerty', 'qwerty')
