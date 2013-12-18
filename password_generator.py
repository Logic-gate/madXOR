#!/usr/bin/env python

# password_generator - generate randome passwords
# original::http://www.emoticode.net/python/custom-random-password-generator.html
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#    * Redistributions of source code must retain the above copyright
#      notice, this list of conditions and the following disclaimer.
#    * Redistributions in binary form must reproduce the above copyright
#      notice, this list of conditions and the following disclaimer in the
#      documentation and/or other materials provided with the distribution.
#    * Neither the name of the <organization> nor the
#      names of its contributors may be used to endorse or promote products
#      derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# Report any issues with this script to <mad_dev@linuxmail.org>

__author__ = ["Tesla", "Ammer Almadani::Mad_Dev"]
__email__  = [" ", "mad_dev@linuxmail.org"]

import string
import random

class Password_Generator:
      
      def shuff(self, passwd):
            shuffle = list(passwd)
            random.shuffle(shuffle)
            passwd = ''.join(shuffle)
            print passwd
            return passwd

      def char_select(self, strg, inp):
            i = 0
            passwd = ''
            while i < inp:
                  passwd += ''.join(random.choice(strg))
                  i += 1
            return passwd

      def digits(self, inp):
            return self.char_select(string.digits, inp)

      def lower(self, inp):
            return self.char_select(string.ascii_lowercase, inp)

      def upper(self, inp):
            return self.char_select(string.ascii_uppercase, inp)

      def special(self, inp):
            return self.char_select(string.punctuation, inp)

      def append(self, file, name, passwd):
            doc = open(file, 'a')
            doc.write('\n'+ name + '::' + passwd + '\n')
            doc.close()