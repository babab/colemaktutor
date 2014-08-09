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

import getch
import os
import random
import sys
import textwrap

try:
    from colors import bold, red, green, cyan, magenta
except ImportError:
    bold = red = green = cyan = magenta = lambda x: x

import colemaktutor.colemaktutor
import colemaktutor.keymapper
import colemaktutor.lessons


class Tutor:
    '''Tutor for the CLI

    The tutor translates lines of text in a lesson into the appropiate
    actions needed for interacting with the user. It also keeps score of
    right/wrong keystrokes.
    '''

    scorePos = 0
    '''The number of right keystrokes'''

    scoreNeg = 0
    '''The number of wrong keystrokes'''

    def __init__(self, mapper):
        '''Load `mapper` and instantiate `Tutor`'''
        self.mapper = mapper

    def lines(self, rows, randomize=False):
        '''Execute `line` for each row, optionally after randomizing words '''
        if not randomize:
            for row in rows:
                self.line(row)
            return self

        # randomize is True
        words = []
        for row in rows:
            self.total += len(row)
            for i in row.split(' '):
                words.append(i)
        random.shuffle(words)

        for line in textwrap.wrap(' '.join(words), 64):
            self.line(line)

    def line(self, row):
        '''For a single line, keep score and interact with the user

        Print the `row` of chars and start a loop where the user tries
        to copy the same chars in sequence, keeping count of the number
        of positive and negative keystrokes. Show the current score in
        numbers and a calculated percentage. Wait for new input until
        all characters in `row` are copied.
        '''
        inp = ''
        output = ''
        scorePos = 0
        scoreNeg = 0

        print (row)
        instr = '--- Copy the line above ---'
        self._scoreOutput(scorePos, scoreNeg, instr, '', row)

        for c in row:
            while True:
                inp = self.mapper.get(getch.getch())
                CLI.write()
                if (inp == c):
                    scorePos += 1
                    self._scoreOutput(scorePos, scoreNeg,
                                      output + green(c), '_', row)
                    output += c
                    break
                scoreNeg += 1
                self._scoreOutput(scorePos, scoreNeg, output, red(inp), row)
        CLI.write()
        self._scoreUpdate(scorePos, scoreNeg)

    def _scoreOutput(self, scorePos, scoreNeg, output, cursor, line):
        perc = lambda neg, ln: str(((ln - neg) / ln) * 100)[:5] + '%'
        score = '({pos} / {neg} / {lineperc})'.format(
            pos=green(str(scorePos)), neg=red(str(scoreNeg)),
            lineperc=cyan(perc(scoreNeg, len(line)))
        )
        CLI.write(output + cursor + ' ' + score)

    def _scoreUpdate(self, scorePos, scoreNeg):
        self.scorePos = scorePos
        self.scoreNeg = scoreNeg


class CLI:
    '''(Interactive) Command Line Interface session'''

    @staticmethod
    def write(text='', end='\r'):
        '''Clear line and print a string, without line feed

        Empty the contents of the current line in terminal (up to 80
        characters). Then print `text` and the suffix `end` which is a
        'carriage return' by default.
        '''
        sys.stdout.write((' ' * 80) + '\r' + text + end)
        sys.stdout.flush()

    @staticmethod
    def inputChar(text='', valid_chars=''):
        '''Get a (valid) character input from the user

        If `valid_chars` contains one or more characters the user will
        be forced to input one of those chars.
        '''
        if text:
            CLI.write(text + '\r')

        if not valid_chars:
            return getch.getch()

        while True:
            inp = getch.getch()
            if inp in valid_chars:
                CLI.write(text + ' ' + inp, end='\n')
                return inp
            wrongtext = red('wrong option')
            CLI.write(text + ' ' + wrongtext if text else wrongtext)

    mapper = None

    def __init__(self, mapper=None):
        if mapper:
            self.mapper = mapper

    def run(self):
        '''Main function for running colemaktutor's interactive CLI'''

        if not self.mapper:
            self.mapper = colemaktutor.keymapper.KeyMapper()
            self.mapper.config(self.layout())

        self.header()
        tutor = Tutor(self.mapper)

        if self.mapper.layout_out == 'colemak':
            headerf = lambda: self.header(self.mapper)
            cl = colemaktutor.lessons.ColemakLessons(
                tutor, header_func=headerf
            )
            headerf()
            start_with_lesson = self.selectLesson(cl.titles)
            cl.start(start_with_lesson)
        else:
            print('That is not available yet, please select another option')
            input('--- Press enter ---')
            self.main()

    def layout(self):
        '''Let the user make a choice between layouts, return layout tuple'''
        print('Colemak tutor allows you to emulate a layout so you can')
        print('learn and practice typing in colemak without installing')
        print('an implementation for your operating system\n')
        print(bold('  1') +
              ' - Practise colemak using a qwerty layout (emulated)')
        print(bold('  2') + ' - Practise colemak using a colemak layout')
        print(bold('  3') +
              ' - Practise qwerty using a colemak layout (emulated)')
        print(bold('  4') + ' - Practise qwerty using a qwerty layout\n')

        inp = CLI.inputChar(bold('Select an option:'), '1234')
        if inp == '1':
            return ('qwerty', 'colemak')
        elif inp == '2':
            return ('colemak', 'colemak')
        elif inp == '3':
            return ('colemak', 'qwerty')
        return ('qwerty', 'qwerty')

    def selectLesson(self, titles):
        '''Let the user choose between available lessons and return lesson #'''
        print('These are the available lessons for this layout\n')
        i = 0
        validChars = ''
        for title in titles:
            i += 1
            iStr = str(i)
            validChars += iStr
            print('  ' + bold(iStr) + ' - ' + title)
        print()
        return int(CLI.inputChar(bold('Select a lesson:'), validChars))

    def header(self, mapper=None):
        '''Clear the terminal screen and print the program header'''
        os.system('cls' if os.name == 'nt' else 'clear')
        print(('=' * 80))
        div = lambda x: ((' ' * x) + '---' + (' ' * x))
        print(bold(colemaktutor.colemaktutor.versionStr) + div(14) + '')

        if mapper:
            print('\nkeyboard layout: in = {in_} / out = {out}'
                  .format(in_=mapper.layout_in, out=mapper.layout_out))
        print(('=' * 80) + '\n')
