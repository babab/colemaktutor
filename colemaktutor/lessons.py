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


class ColemakLessons:
    def __init__(self, tutor, header_func, start=1):
        self.tutor = tutor
        self.header_func = header_func
        if start == 1:
            self.lesson1()
        self.lesson2()

    def lesson1(self):
        self.header_func()
        print('Lesson 1 - letters STNE\n')
        print('      --ST--NE---        --DF--JK---')
        print('         *  *               *  *')
        print('       (colemak)          (qwerty)\n')
        self.tutor.lines([
            'sets tens ten tnt sestet tenet seen nene testee tenets',
            'essen sent senses tenses teens stent sense tent nets',
            'tenseness net tense nests tennessee teen nest tents',
            'net tens teen tenets senses nests nest nets tenet',
            'sent sense tenses tennessee essen tnt tent teens',
            'tense nene stent seen'
        ])

    def lesson2(self):
        self.header_func()
        print('Lesson 2 - letters RI\n')
        print('      -RST--NEI--        -SDF--JKL--')
        print('         *  *               *  *')
        print('       (colemak)          (qwerty)\n')
        self.tutor.lines([
            'trite stress sire it entire terse tit sir tire sinner retire',
            'rinse inn tree insist tier rite teeter resin stir siren enter',
            'sitter insert site sneer intern tie inner series steer tin',
            'riser its resent sin rise rent rein iris stern in titter resist',
            'eerie inert street is renter sit nine risen sister serene',
            'stint err snit intent entree nit inter rest tennis re tint'
        ])
