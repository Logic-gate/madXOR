#!/usr/bin/env python

# vault51 - generate random passwords and encrypt them 
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

__author__ = ["Ammer Almadani::Mad_Dev"]
__email__  = ["mad_dev@linuxmail.org"]

import password_generator
import xor
import os
import shutil
import sys
import time
import argparse
import datetime
import ConfigParser


class vault51:

	def create(self, file, name, digits, lower, upper, special):
		'''Example::
		pg.append('password.txt', 'john@twitter', pg.shuff(pg.digits(4)+pg.lower(4)+pg.upper(3)+pg.special(3)))
		'''
		pg = password_generator.Password_Generator()
		x = xor.Xor()

		if os.path.isfile('my_settings.dat'):
			x.decrypt(file+'_encrypted', file+'.key', file)
       

		print 'Generating Password'
		pg.append(file, name, pg.shuff(pg.digits(digits)+pg.lower(lower)+pg.upper(upper)+pg.special(special)))
		print 'Saved in %s with %s as an identifier' %(file, name)

		print 'Encrypting %s' %file
		sys.stdout.flush()

		self.update_progress_bar()
		x.encrypt(file, file+'_encrypted', file+'.key', 2)

		self.update_progress_bar()
		not_needed = [file]
		for i in not_needed:
			os.remove(i)

		self.update_progress_bar()
		print ' Done!'

	def update_progress_bar(self):
		print '\b.',
		sys.stdout.flush()

	def retrieve(self, file):

		x = xor.Xor()
		print 'Decrypting %s' %file
		sys.stdout.flush()

		self.update_progress_bar()
		x.decrypt(file+'_encrypted', file+'.key', file)

		self.update_progress_bar()
		not_needed = [file+'.key', file+'_encrypted']
		for i in not_needed:
			os.remove(i)

		self.update_progress_bar()
		print ' Done!'

		print 'Showing Content::'

		a = open(file)
		print a.read()
		a.close()

	def encrypt(self, file):
		x = xor.Xor()
		x.encrypt(file, file+'_encrypted', file+'.key', 2)
		not_needed = [file]
		for i in not_needed:
			os.remove(i)



if __name__ == '__main__':
	v = vault51()

	parser = argparse.ArgumentParser(prog=__file__, description = 'Generate random passwords and encrypt them. The default name for the encrypted file is file_encrypted. The default name for the key is file.key',
		formatter_class=argparse.ArgumentDefaultsHelpFormatter, 
		epilog='Run '+__file__+' without arguments to retrieve the file. This is a beta version')
	parser.add_argument("-d", metavar = "", type = int, help = "number of digits")
	parser.add_argument("-l", metavar = "", type = int, help = "number of lower case char")
	parser.add_argument("-u", metavar = "", type = int, help = "number of upper case char")
	parser.add_argument("-s", metavar = "", type = int, help = "number of spacial char")
	parser.add_argument("-o", metavar = "", help = "path to store the password")
	parser.add_argument("-n", metavar = "", help = "name to append")
	parser.add_argument("-edit", metavar = "", help = "manually edit file")

	if len(sys.argv) == 1:
		f = raw_input('Please Input File Name: ')
		v.retrieve(f)
		v.encrypt(f)
		sys.exit(0)

	args = parser.parse_args()

	if args.edit is not None:
		v.retrieve(args.edit)
		os.system('nano %s' %args.edit)
		v.encrypt(args.edit)
		sys.exit(0)

	if args.d is not None:
		digit = args.d
	else:
		digit = 0
	if args.l is not None:
		lower = args.l
	else:
		lower = 0
	if args.u is not None:
		upper = args.u
	else:
		upper = 0
	if args.s is not None:
		special = args.s
	else:
		special = 0

	v.create(args.o, args.n, int(digit), int(lower), int(upper), int(special))

