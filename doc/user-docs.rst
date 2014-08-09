User documentation
==============================================================================

colemaktutor is written in Python_ and uses the following Python_
packages:

 - getch_
 - *Optional*: ansicolors_ (for terminal color support)

.. note:: At this moment colemaktutor is in an early development stage.
          Until a first release is made you can try the development
          version.

Install dependencies
--------------------

If you have pip_ installed, you can run (optionally in a virtualenv)::

   $ (sudo) pip install -r requirements.txt

Otherwise, install the following packages manually:

 - getch_
 - ansicolors_ (optional)

Install colemaktutor
--------------------

If you have make_, and pip_ installed, you can run (optionally in
a virtualenv)::

   $ (sudo) PYTHON_EXEC=python PIP_EXEC=pip make install

Otherwise, you can install/update colemaktutor by running:

- Using pip_::

	$ (sudo) python setup.py sdist
	$ (sudo) pip install --upgrade dist/colemaktutor-0.1.0.tar.gz

- Manually::

   $ (sudo) python setup.py install

Using colemaktutor
------------------

Just run ``colemaktutor``, you will be guided by the program.

Uninstall colemaktutor (pip only)
---------------------------------

Easily uninstall colemaktutor if you've installed it using pip with::

   $ (sudo) pip uninstall colemaktutor

.. external references .......................................................
.. _Python: https://www.python.org/downloads/
.. _getch: https://pypi.python.org/pypi/getch
.. _ansicolors: https://pypi.python.org/pypi/ansicolors
.. _pip: https://pypi.python.org/pypi/pip
.. _make: http://en.wikipedia.org/wiki/Make_(software)
