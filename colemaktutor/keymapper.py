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
