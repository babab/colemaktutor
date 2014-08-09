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

PYTHON_EXEC		= python
PIP_EXEC		= pip

sinclude config.mk

VERSION		= 0.1.0

make:
	@echo "make install   Build and then install via pip and move manpage"
	@echo "make uninstall Clean build files and uninstall via pip"
	@echo
	@echo "Developer commands"
	@echo "make doc       Build html documentation"
	@echo "make dist      Build python source archive file"
	@echo "make clean     Clean program build files"

rm_pyc:
	find . -name "*.pyc" | xargs /bin/rm -f

dist: rm_pyc
	$(PYTHON_EXEC) setup.py sdist

install: dist
	$(PIP_EXEC) install --upgrade dist/colemaktutor-$(VERSION).tar.gz
	make clean

uninstall: clean
	$(PIP_EXEC) uninstall colemaktutor

clean:
	rm -f MANIFEST
	rm -rf dist

docs: install
	(cd doc && make html)

# vim: set noet ts=8 sw=8 sts=8:
