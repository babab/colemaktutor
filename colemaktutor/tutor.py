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

from getch import getch

from colors import (
    red,
    green,
    # magenta,
    # cyan,
    # underline,
    # bold,
)

import cli


class CLITutor:
    scorePos = 0
    scoreNeg = 0

    def __init__(self, mapper):
        self.mapper = mapper

    def lines(self, rows):
        for row in rows:
            self.line(row)

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
