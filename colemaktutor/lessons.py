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

try:
    from colors import green, cyan, bold, underline
except ImportError:
    green = cyan = bold = underline = lambda x: x


class ColemakLessons:
    titles = [
        'Lesson 1 - letters ' + green('STNE'),
        'Lesson 2 - letters ' + green('RI'),
        'Lesson 3 - letters ' + green('AO'),
    ]

    def __init__(self, tutor, header_func):
        self.tutor = tutor
        self.header_func = header_func

    def start(self, start=1):
        n = 0
        for i in self.titles:
            n += 1
            if start <= n:
                getattr(self, 'lesson' + str(n))()

    def printHeader(self, lessonNum):
        self.header_func()
        print(self.titles[lessonNum - 1] + '\n')

    def lesson1(self):
        self.printHeader(1)
        # print('      --ST--NE---        --DF--JK---')
        print(
            '      '
            '--' + green('S') + green('T', style='underline') + '-'
            '-' + green('N', style='underline') + green('E') + '---'
            '        '
            '-SD' + underline('F') + '--' + underline('J') + 'KL--'
        )
        print('\n       (colemak)          (qwerty)\n')
        self.tutor.lines([
            'sets tens ten tnt sestet tenet seen nene testee tenets',
            'essen sent senses tenses teens stent sense tent nets',
            'tenseness net tense nests tennessee teen nest tents',
            'net tens teen tenets senses nests nest nets tenet',
            'sent sense tenses tennessee essen tnt tent teens',
            'tense nene stent seen'
        ])

    def lesson2(self):
        self.printHeader(2)
        # print('      -RST--NEI--        -SDF--JKL--')
        print(
            '      '
            '-' + green('R') + cyan('S') + cyan('T', style='underline') + '-'
            '-' + cyan('N', style='underline') + cyan('E') + green('I') + '--'
            '        '
            '-SD' + underline('F') + '--' + underline('J') + 'KL--'
        )
        print('\n       (colemak)          (qwerty)\n')
        self.tutor.lines([
            'trite stress sire it entire terse tit sir tire sinner retire',
            'rinse inn tree insist tier rite teeter resin stir siren enter',
            'sitter insert site sneer intern tie inner series steer tin',
            'riser its resent sin rise rent rein iris stern in titter resist',
            'eerie inert street is renter sit nine risen sister serene',
            'stint err snit intent entree nit inter rest tennis re tint'
        ])

    def lesson3(self):
        self.printHeader(3)
        # print('      ARST--NEIO-        ASDF--JKL;-')
        print(
            '      '
            + green('A') + cyan('RS') + cyan('T', style='underline') + '-'
            '-' + cyan('N', style='underline') + cyan('EI') + green('O') + '-'
            '        '
            'ASD' + underline('F') + '--' + underline('J') + 'KL;-'
        )
        print('\n       (colemak)          (qwerty)\n')
        self.tutor.lines([
            'retain roe rant ratio toast sort stat tore earn noose',
            'teat eater oat trio tear tone artist nor tattoo seat arise',
            'noise start toss tenant oasis one aria no arson sonata ',
            'soon rear to ass soot irate sane onset star root state',
            'oar errant resort tartan sonnet notes eat rotten stain',
            'ration arose reason noon sass retina iota torn stairs',
            'iron estate toe are season not attire tenor innate',
            'torso tease arisen note tar snort tarot',
        ])
