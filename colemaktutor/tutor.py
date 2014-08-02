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

import random
import textwrap
from getch import getch

try:
    from colors import red, green
except ImportError:
    red = green = lambda x: x

import cli


class CLITutor:
    scorePos = 0
    scoreNeg = 0

    def __init__(self, mapper):
        self.mapper = mapper

    def lines(self, rows, randomize=False):
        if not randomize:
            for row in rows:
                self.line(row)
            return self

        # randomize is True
        words = []
        for row in rows:
            for i in row.split(' '):
                words.append(i)
        random.shuffle(words)

        for line in textwrap.wrap(' '.join(words), 64):
            self.line(line)

    def line(self, row):
        inp = ''
        output = ''
        scorePos = 0
        scoreNeg = 0

        print (row)
        cli.write('--- Copy the line above ---')

        for c in row:
            while True:
                inp = self.mapper.get(getch())
                cli.write()
                if (inp == c):
                    scorePos += 1
                    self._scoreOutput(scorePos, scoreNeg,
                                      output + green(c), '_')
                    output += c
                    break
                scoreNeg += 1
                self._scoreOutput(scorePos, scoreNeg, output, red(inp))
        cli.write()
        self._scoreUpdate(scorePos, scoreNeg)

    def _scoreOutput(self, scorePos, scoreNeg, output, cursor):
        score = '({pos}/{neg})'.format(pos=green(str(scorePos)),
                                       neg=red(str(scoreNeg)))
        cli.write(output + cursor + ' ' + score)

    def _scoreUpdate(self, scorePos, scoreNeg):
        self.scorePos = scorePos
        self.scoreNeg = scoreNeg

if __name__ == '__main__':
    class TestMapper:
        def get(self, x):
            return x

    test_lines = [
        'sets tens ten tnt sestet tenet seen nene testee tenets',
        'essen sent senses tenses teens stent sense tent nets',
        'tenseness net tense nests tennessee teen nest tents',
        'net tens teen tenets senses nests nest nets tenet',
        'sent sense tenses tennessee essen tnt tent teens',
        'tense nene stent seen'
    ]

    CLITutor(TestMapper()).lines(test_lines, randomize=True)
