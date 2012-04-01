# Emacs-like Sublime Modeline

Parse Emacs-like modelines, and set buffer-local settings.


## Installing

I highly recommend installing via [Package Control](http://wbond.net/sublime_packages/package_control).


## Usage

Somewhere within the first five lines of a file, add a line matching the following:

	-*- key: value; key2: value2 -*-

or

	-*- syntax -*-

Currently, only '`mode`', '`tab-width`' and '`indent-tabs-mode`' are supported.

The values for '`mode`' are the root filename of the .tmLanaguge file. Most of
the time these are obvious and match the syntax name but not all the time. For
example the 'Graphviz (DOT)' syntax is simply 'dot'. To find out the correct
value you can run this command in the console (ctrl+\`) when the syntax you want is in
use:

	view.settings().get('syntax')
	# u'Packages/Graphviz/DOT.tmLanguage' -> 'DOT' is the mode value needed.

## Alternatives

* [Vim-style modelines](https://github.com/SublimeText/Modelines)
* [More Emacs-style hacks](http://software.clapper.org/ST2EmacsMiscellanea/)
